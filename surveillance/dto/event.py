from typing_extensions import TypedDict, Literal, Any, List

EventNames = Literal[Literal['person-enter'], Literal['person-leave']]

Severity = Literal[Literal['critical'], Literal['warning'], Literal['info']]


class Event(TypedDict):
    device: List[int] | int
    data: Any


class ExtendedEvent(Event, TypedDict):
    name: EventNames
    severity: Severity


EventDTO = Event | ExtendedEvent
