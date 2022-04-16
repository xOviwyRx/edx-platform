from django.urls import path
from .views import greeting_view

urlpatterns = [
    path("greeting_app/", greeting_view, name="greeting_app"),
]
