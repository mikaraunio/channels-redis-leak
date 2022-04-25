import os

from asgiref.sync import async_to_sync
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

import django
from django.urls import path

TESTGROUP = 'TESTGROUP'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings')
django.setup()

class TestAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(TESTGROUP, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(TESTGROUP, self.channel_name)


class TestConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(TESTGROUP, self.channel_name)
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(TESTGROUP, self.channel_name)


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('socket/test', TestAsyncConsumer.as_asgi()),
        # path('socket/test', TestConsumer.as_asgi()),
    ]),
})
