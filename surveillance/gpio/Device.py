from typing_extensions import Any

from surveillance.ApiSubject import ApiSubject
from surveillance.dto.event import EventDTO, Event


class Device(ApiSubject):
    actor_count: int = 0
    device_list: list = []

    def __init__(self, pin: int, **kwds):
        Device.actor_count += 1
        self.id: int = Device.actor_count
        self.pin: int = pin
        Device.device_list.append(self)
        super().__init__(**kwds)

    def notify(self, payload: Any):
        event: EventDTO = Event(device=self.id, data=payload)
        super().notify(event)