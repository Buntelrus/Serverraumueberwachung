from typing_extensions import Any

from surveillance.ApiSubject import ApiSubject
from surveillance.dto.device import DeviceDTO
from surveillance.dto.event import EventDTO


class Device(ApiSubject):
    actor_count: int = 0
    device_list: list[DeviceDTO] = []

    def __init__(self, pin: int = 0, **kwds):
        Device.actor_count += 1
        self.id: int = Device.actor_count
        self.pin: int = pin
        Device.device_list.append(DeviceDTO(
            id=self.id,
            name=self.name,
            description=self.description,
            value=self.value
        ))
        super().__init__(**kwds)

    def notify(self, payload: Any):
        event: EventDTO = EventDTO(device=self.id, data=payload)
        super().notify(event)