from django.urls import path
from .consumers import (
    MySyncConsumer,
    MyAsyncConsumer,
    MyWebsocketConsumer,
    MyAsyncWebsocketConsumer,
    MyJsonWebSocketConsumer,
    MyAsyncJsonWebSocketConsumer,
)

websocket_urlpatterns = [
    path('ws/sc/', MySyncConsumer.as_asgi()),
    path('ws/ac/', MyAsyncConsumer.as_asgi()),

    path('ws/mwc/', MyWebsocketConsumer.as_asgi()),
    path('ws/mawc/', MyAsyncWebsocketConsumer.as_asgi()),

    path('ws/mjwc/', MyJsonWebSocketConsumer.as_asgi()),
    path('ws/majwc/', MyAsyncJsonWebSocketConsumer.as_asgi()),

]
