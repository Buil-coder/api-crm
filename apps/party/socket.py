import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class client_socket(AsyncWebsocketConsumer):
    async def connect(self):
        tenant = self.scope["url_route"]["kwargs"]["tenant"]

        self.room_name = "client_{}".format(tenant.lower().replace(" ", ""))
        self.room_group_name = "ws_{}".format(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def send_message(self, event): await self.send(text_data=json.dumps(event['message']))

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'send_message', 'message':text_data}
        )

    @classmethod
    def notify(self, message:str, tenant:str):
        self.room_name = "client_{}".format(tenant.lower().replace(" ", ""))
        self.room_group_name = "ws_{}".format(self.room_name)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            self.room_group_name,
            { 'type': 'send_message', 'message': message }
        )