import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from chat.models import ChatThread, ChatMessage

fake = Faker()


def create_users(n=5):
    users = []
    for _ in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
        users.append(user)
    return users


def create_threads(users):
    threads = []
    for i in range(len(users) - 1):
        thread = ChatThread.objects.create()
        thread.participants.set([users[i], users[i + 1]])
        threads.append(thread)
    return threads


def create_messages(threads):
    for thread in threads:
        for _ in range(5):
            ChatMessage.objects.create(
                thread=thread,
                sender=thread.participants.all()[0],
                text=fake.text(),
                is_read=fake.boolean()
            )


def main():
    users = create_users()
    threads = create_threads(users)
    create_messages(threads)
    print("Database filled with fake data!")


if __name__ == '__main__':
    main()
