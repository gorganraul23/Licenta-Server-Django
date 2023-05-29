import json

from channels.generic.websocket import AsyncWebsocketConsumer


class SensorDataConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send("Connection established with Django")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # Process the received message from Unity if needed
        print("Received: ", text_data)
        await self.send_message()

    async def send_message(self):
        # await self.send(json.dumps({'message': message}))
        await self.send("Sent from Django today !!!")


class AngularConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_name = self.scope['url_route']['kwargs']['channel_name']
        await self.channel_layer.group_add(self.channel_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.channel_name, self.channel_name)

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        print(text_data)

        await self.send(text_data=json.dumps({'message': text_data}))

    async def send_data(self, event):
        message = event['message']
        print('Message: ', message)
        await self.send(text_data=json.dumps({'message': message}))
