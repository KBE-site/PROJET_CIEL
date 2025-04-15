from django.urls import re_path
from .consumers import APIConsumerSun

websocket_urlpatterns = [
    re_path(r'ws/api/$', APIConsumerSun.as_asgi()),
]