import json

from typing_extensions import List

from surveillance.Subject import Subject, SubscriptionArguments
from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.event import EventDTO


class ApiSubject(Subject):
    event_list: List[EventDTO] = []
    def __init__(self, websocket_manager: WebSocketManager, **kwds):
        self.websocket_manager = websocket_manager
        super().__init__(**kwds)

    async def notify(self, payload: EventDTO):
        super().notify(payload)
        ApiSubject.event_list.append(payload)
        await self.websocket_manager.broadcast("test")
