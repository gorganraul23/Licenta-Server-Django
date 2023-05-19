from channels.generic.websocket import AsyncWebsocketConsumer


class SensorDataConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send("Connection established with Unity")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process the received message from Unity if needed
        print("Received: ", text_data)
        await self.send_message(text_data)
        pass

    async def send_message(self, message):
        await self.send(message)
        # await self.send(json.dumps(data))
        # message = event['message']
        # print("Sending data:")

        # await self.send('Hello')
