from django.urls import path
from .views import index, newform

urlpatterns = [
    path("", index),
    path("newform/", newform),
]