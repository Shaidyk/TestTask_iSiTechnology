from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from chat.models import ChatThread, ChatMessage
from chat.serializers.chat_message_serializer import ChatMessageSerializer


class ChatMessageCreateView(generics.CreateAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        thread = serializer.validated_data.get('thread')

        if not thread.participants.filter(id=self.request.user.id).exists():
            raise PermissionDenied("You are not a participant of this thread.")

        serializer.save(sender=self.request.user)


class ChatMessageListView(generics.ListAPIView):
    """
    Retrieves a list of messages for a specific thread.
    Validates that the authenticated user is a participant in the thread.
    Supports pagination.
    """
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        thread = ChatThread.objects.get(id=thread_id)

        if not thread.participants.filter(id=self.request.user.id).exists():
            raise PermissionDenied("You are not a participant of this thread.")

        return ChatMessage.objects.filter(thread=thread)


class ChatMessageMarkAsReadView(generics.UpdateAPIView):
    """
    Marks a message as read.
    Validates that the authenticated user is a participant in the thread.
    """
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        message = self.get_object()
        thread = message.thread

        if not thread.participants.filter(id=self.request.user.id).exists():
            raise PermissionDenied("You are not a participant of this thread.")

        serializer.save()


class UnreadMessagesCountView(generics.GenericAPIView):
    """
    Returns the number of unread messages for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        unread_count = ChatMessage.objects.filter(
            thread__participants=request.user,
            is_read=False
        ).exclude(sender=request.user).count()

        return Response({'unread_count': unread_count})
