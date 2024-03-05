import asyncio

from typing_extensions import List, Any

from surveillance.Subject import Subject
from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.event import EventDTO, Event
from surveillance.gpio.Device import Device


class ApiSubject(Subject, Device):
    event_list: List[EventDTO] = []
    def __init__(self, websocket_manager: WebSocketManager, **kwds):
        self.websocket_manager = websocket_manager
        super().__init__(**kwds)

    def notify(self, payload: Any):
        event: EventDTO = Event(device=self.id,data=payload)
        super().notify(event)
        ApiSubject.event_list.append(event)
        asyncio.ensure_future(self.websocket_manager.broadcast(event), loop=asyncio.get_event_loop())