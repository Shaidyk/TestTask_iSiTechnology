from django.contrib import admin

from chat.models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'sender', 'text', 'created', 'is_read')
    list_filter = ('is_read', 'created')
    search_fields = ('text', 'sender__username')
