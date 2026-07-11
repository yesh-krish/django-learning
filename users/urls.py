from django.urls import path
from users.views import register_view  # <-- Import the specific function directly

app_name = 'users'
urlpatterns = [
    path('register/', register_view, name='register'),
]
