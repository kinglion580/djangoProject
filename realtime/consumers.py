import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class LogConsumer(WebsocketConsumer):
    def connect(self):
        print(self.channel_layer)
        print(self.channel_name)
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
