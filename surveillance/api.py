from typing import Union, List

from fastapi import FastAPI
from starlette.websockets import WebSocket

from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.event import EventDTO, Event, ExtendedEvent

app = FastAPI()
websocket_manager = WebSocketManager()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/events")
def events() -> List[EventDTO]:
    return [
        Event(
            actor=12,
            data="test"
        ),
        ExtendedEvent(
            actor=13,
            data="wow",
            severity='warning',
            name='person-enter'
        )
    ]


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await WebSocketManager.connect(websocket)