# 📡 Django Signals & ORM – Advanced Messaging Features

This project demonstrates advanced Django features using **signals, custom managers, ORM techniques, and caching** to build a fully functional messaging system.

---

## 🗂️ Project Structure
alx-backend-python/
├── Django-signals_orm-0x04/
│ ├── messaging/
│ │ ├── models.py
│ │ ├── signals.py
│ │ ├── apps.py
│ │ ├── admin.py
│ │ ├── tests.py
│ │ ├── views.py
│ ├── Django-signals_orm-0x04/
│ │ ├── settings.py
│ ├── Django-Chat/
│ │ ├── views.py


---

## Task 0: 📩 Signal for User Notifications

**Objective:** Notify users when they receive a new message.

### ✅ Features:
- `Message` model: sender, receiver, content, timestamp
- `Notification` model: linked to message and receiver
- `post_save` signal: auto-creates a notification on new message

### 📁 Files:
- `messaging/models.py`, `messaging/signals.py`, `messaging/apps.py`

### 📊 Schema:

User ──┬────────────▶ Message ◀──────────┬── User
       │                                  │
       └──▶ Notification ◀───────────────┘


---

## Task 1: ✏️ Signal for Logging Message Edits

**Objective:** Track when messages are edited and log old content.

### ✅ Features:
- `edited` field in `Message`
- `MessageHistory` model stores pre-edit content
- `pre_save` signal logs content before update

### 📁 Files:
- `Django-Chat/models.py`, `Django-Chat/signals.py`

### 📊 Schema:
Message ────┬────▶ MessageHistory
            └────[edited=True if modified]


---

## Task 2: 🧹 Delete User-Related Data via Signal

**Objective:** Cleanup all related data when a user is deleted.

### ✅ Features:
- `delete_user` view
- `post_delete` signal on `User`
- Deletes messages, notifications, histories

### 📁 Files:
- `Django-Chat/views.py`, `Django-Chat/signals.py`

### 📊 Schema:

User (deleted)
├───┬──▶ Message
│   └──▶ MessageHistory
└───▶ Notification


---

## Task 3: 🧵 Threaded Conversations with ORM Optimization

**Objective:** Implement message replies (threading) using self-referencing models.

### ✅ Features:
- `parent_message` field (self-FK)
- Recursive function to fetch replies
- `select_related` + `prefetch_related` for optimization

### 📁 Files:
- `Django-Chat/models.py`, `messaging/views.py`

### 📊 Schema:
Message
└── replies (Message)
└── replies (Message)


---

## Task 4: 📥 Custom ORM Manager for Unread Messages

**Objective:** Filter and optimize unread messages for a user.

### ✅ Features:
- `read` field in `Message`
- `UnreadMessagesManager` with `unread_for_user(user)`
- `.only()` used to reduce query size

### 📁 Files:
- `Django-Chat/models.py`, `messaging/managers.py`, `messaging/views.py`

### 📊 Schema:



---

## Task 5: 🧠 Implement Basic View Cache

**Objective:** Add caching to message views for performance.

### ✅ Features:
- `LocMemCache` setup in `settings.py`
- `@cache_page(60)` for message list view

### 📁 Files:
- `messaging_app/settings.py`, `chats/views.py`

### 🔁 Caching Example:
```python
@cache_page(60)
def conversation_view(request):
    ...

### ✅ Final Notes
- Use python manage.py makemigrations && migrate after model changes.
- Run python manage.py test to ensure functionality.
- Templates should be updated to render threaded conversations and histories.


