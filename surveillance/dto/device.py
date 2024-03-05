from typing_extensions import TypedDict


class TemperatureDTO(TypedDict):
    temperature: float
    humidity: float


class DeviceDTO(TypedDict):
    id: int
    name: str
    description: str
    value: bool | TemperatureDTO
