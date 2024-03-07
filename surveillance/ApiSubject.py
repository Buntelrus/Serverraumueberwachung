import asyncio

from typing_extensions import List, Any

from surveillance.Subject import Subject
from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.event import EventDTO


class ApiSubject(Subject):
    event_list: List[EventDTO] = []

    def __init__(self, websocket_manager: WebSocketManager, **kwds):
        self.websocket_manager = websocket_manager
        super().__init__(**kwds)

    def notify(self, payload: Any):
        super().notify(payload)
        ApiSubject.event_list.append(payload)
        loop=asyncio.get_event_loop()
        asyncio.ensure_future(self.websocket_manager.broadcast(payload), loop=asyncio.get_event_loop())
