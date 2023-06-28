import json

from channels.generic.websocket import AsyncWebsocketConsumer


class SensorDataConsumer(AsyncWebsocketConsumer):

    connected = False

    async def connect(self):
        self.connected = True
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        print("Received: ", text_data)

    async def send_message(self, hr, hrv, message):
        await self.send(json.dumps({'hr': hr, 'hrv': hrv, 'message': message}))


class AngularConsumer(AsyncWebsocketConsumer):

    connected = False

    async def connect(self):
        self.connected = True
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)

    async def send_data(self, hr, hrv):
        await self.send(json.dumps({'hr': hr, 'hrv': hrv}))
