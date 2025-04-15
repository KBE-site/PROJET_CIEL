import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.rc import rc
from time import sleep
import asyncio

class APIConsumerSun(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            data = json.loads(rc().text)
            await self.send(json.dumps({'api_altitude': data.get("altitude"), 'api_azimuth': data.get("azimuth")}))
            await asyncio.sleep(1)