from rest_framework import serializers

from chat.models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = ChatMessage
        fields = '__all__'
        extra_kwargs = {'sender': {'required': False}}
