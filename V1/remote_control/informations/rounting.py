from django.urls import re_path
from .consumers import InformationsConsumer

websocket_urlpatterns = [
    re_path(r"ws/informations/(?P<room_name>\w+)/$", InformationsConsumer.as_asgi())
]