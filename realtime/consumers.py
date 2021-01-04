import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class LogConsumer(WebsocketConsumer):
    def connect(self):
        user_uuid = self.scope["session"]["current_user"]
        print(user_uuid)
        async_to_sync(self.channel_layer.group_add)(
            user_uuid,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        user_uuid = self.scope["session"]["current_user"]
        async_to_sync(self.channel_layer.group_discard)(
            user_uuid,
            self.channel_name
        )

    def chat_message(self, event):
        self.send(text_data=event['text'])
