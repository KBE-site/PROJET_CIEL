import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.rc import APIStellarium
import asyncio

class InformationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.accept()

        while True:
            api = APIStellarium(self.room_name)
            data = json.loads(api.get_all_object_informations())
            await self.send(json.dumps({'api_altitude': data.get("altitude"), 'api_azimuth': data.get("azimuth")}))
            await asyncio.sleep(1)