# Simple Chat API

## Description
This is a simple REST API for a two-user chat application. It allows creating threads (dialogues), sending messages, retrieving message and thread lists, marking messages as read, and counting unread messages.

## Installation

```bash
git clone <repository_url>
cd <project_directory>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Optional
python manage.py loaddata db_dump.json  # Optional
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/token/` – Obtain JWT token
- `POST /api/token/refresh/` – Refresh JWT token

### Threads
- `POST /api/chat/threads/create/` – Create a thread or return existing
- `GET /api/chat/threads/` – List user threads
- `DELETE /api/chat/threads/<id>/delete/` – Delete a thread

### Messages
- `POST /api/chat/messages/create/` – Create a message
- `GET /api/chat/threads/<thread_id>/messages/` – List thread messages
- `PATCH /api/chat/messages/<id>/read/` – Mark message as read
- `GET /api/chat/messages/unread_count/` – Get unread messages count

## Pagination
All list endpoints support `limit` and `offset` query parameters.

Example:

```bash
GET /api/chat/threads/?limit=5&offset=0
```

## Admin Panel
Access at: `http://127.0.0.1:8000/admin/`

## Running Tests

```bash
python manage.py test
```

## License
This project is licensed under the MIT License.