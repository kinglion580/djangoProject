import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class LogConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'test_group',
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            'test_group',
            self.channel_name
        )

    def chat_message(self, event):
        self.send(text_data=event['text'])


class AsyncLogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'test_group',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            'test_group',
            self.channel_name
        )

    async def chat_message(self, event):
        await self.send(text_data=event['text'])
