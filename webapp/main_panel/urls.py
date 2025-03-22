from django.urls import path, re_path
from .views import index, move, room_object

urlpatterns = [
    path('', index, name='index'),
    path('move/', move, name='move'),
    re_path(r'<str:room_name>/', room_object, name="room_object"),
]