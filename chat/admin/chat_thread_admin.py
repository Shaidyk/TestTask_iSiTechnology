from django.contrib import admin

from chat.models import ChatThread


@admin.register(ChatThread)
class ChatThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_participants', 'created', 'updated')

    def display_participants(self, obj):
        return ', '.join([user.username for user in obj.participants.all()])
    display_participants.short_description = 'Participants'
