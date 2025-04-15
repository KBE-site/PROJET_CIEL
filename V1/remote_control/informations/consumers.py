import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.rc import rc
import asyncio

class InformationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.accept()

        while True:
            data = json.loads(rc(self.room_name).text)
            await self.send(json.dumps({'api_altitude': data.get("altitude"), 'api_azimuth': data.get("azimuth")}))
            await asyncio.sleep(1)