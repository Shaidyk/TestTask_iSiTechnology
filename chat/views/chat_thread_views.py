from django.db.models import Count
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chat.models import ChatThread
from chat.serializers.chat_thread_serializer import ChatThreadSerializer


class ChatThreadCreateView(generics.CreateAPIView):
    """
    Creates a thread between two users.
    If a thread with these users already exists, returns the existing thread.
    """
    serializer_class = ChatThreadSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        participant_ids = request.data.get('participants', [])

        if len(participant_ids) != 2:
            return Response(
                {"error": "Thread must have exactly 2 participants."},
                status=status.HTTP_400_BAD_REQUEST
            )

        participants = sorted(participant_ids)
        existing_thread = ChatThread.objects.annotate(num_participants=Count('participants')).filter(
            num_participants=2,
            participants__id=participants[0],
        ).filter(participants__id=participants[1]).first()

        if existing_thread:
            serializer = self.get_serializer(existing_thread)
            return Response(serializer.data)

        thread = ChatThread.objects.create()
        thread.participants.set(participant_ids)
        serializer = self.get_serializer(thread)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChatThreadListView(generics.ListAPIView):
    """
    Retrieves the list of threads for the authenticated user.
    """
    serializer_class = ChatThreadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChatThread.objects.filter(participants=self.request.user)


class ChatThreadDeleteView(generics.DestroyAPIView):
    """
    Deletes a thread by its ID.
    Only authorized users can delete threads.
    """
    queryset = ChatThread.objects.all()
    permission_classes = [IsAuthenticated]
