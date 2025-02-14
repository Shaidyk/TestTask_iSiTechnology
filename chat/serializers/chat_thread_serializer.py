from rest_framework import serializers

from chat.models import ChatThread


class ChatThreadSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = ChatThread
        fields = '__all__'
