from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from channel1 import consumer

ws_pattern= [
    path('ws/tableData/', consumer.TableData.as_asgi()),
]

application= ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(ws_pattern))
    }
)