from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/wsc/<str:roomName>/', consumers.MyWebsocketConsumer.as_asgi())
]
