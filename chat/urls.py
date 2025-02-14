from django.urls import path
from chat.views import (
    ChatThreadCreateView, ChatThreadListView, ChatThreadDeleteView,
    ChatMessageCreateView, ChatMessageListView, ChatMessageMarkAsReadView,
    UnreadMessagesCountView,
)

urlpatterns = [
    # Threads
    path('threads/', ChatThreadListView.as_view(), name='thread-list'),
    path('threads/create/', ChatThreadCreateView.as_view(), name='thread-create'),
    path('threads/<int:pk>/delete/', ChatThreadDeleteView.as_view(), name='thread-delete'),

    # Messages
    path('threads/<int:thread_id>/messages/', ChatMessageListView.as_view(), name='message-list'),
    path('messages/create/', ChatMessageCreateView.as_view(), name='message-create'),
    path('messages/<int:pk>/read/', ChatMessageMarkAsReadView.as_view(), name='message-mark-read'),
    path('messages/unread_count/', UnreadMessagesCountView.as_view(), name='unread-count'),
]
