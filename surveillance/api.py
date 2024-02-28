import asyncio
import time
from typing import Union, List

from fastapi import FastAPI
from starlette.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware

from surveillance.PersonCounter import PersonCounter
from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.event import EventDTO, Event, ExtendedEvent

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://buntelrus.github.io",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
websocket_manager = WebSocketManager()

# personCounter = PersonCounter(websocket_manager)
# async def send_event():
#     print("interval")
#     await websocket_manager.broadcast("test")
#     await asyncio.sleep(3)
# @app.on_event("startup")
# async def startup_event():
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(send_event())
#     try:
#         loop.run_until_complete(task)
#     except asyncio.CancelledError:
#         pass
#     print("went here")

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
    await websocket_manager.connect(websocket)
    while True:
        print("interval")
        await websocket_manager.broadcast("test")
        await asyncio.sleep(3)