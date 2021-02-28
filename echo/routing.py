from django.urls import path
from .consumers import EchoConsumer, ChatConsumer

websocket_urlpatterns = [
    path('ws/', EchoConsumer.as_asgi(), name='echo_consumer'),
    path('ws/chat/<str:username>/', ChatConsumer.as_asgi(), name='chat_consumer'),
]
