import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
from app.models import Ai1, Ai2


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            choice_query_set_1 = await sync_to_async(list)(Ai1.objects.values())
            choice_query_set_2 = await sync_to_async(list)(Ai2.objects.values())
            await self.send(json.dumps({'value_1': choice_query_set_1,'value_2': choice_query_set_2}))
            await sleep(1)

