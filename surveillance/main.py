import asyncio
from typing import Union, List

from fastapi import FastAPI
from starlette.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware

from surveillance.ApiSubject import ApiSubject
from surveillance.PersonCounter import PersonCounter
from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.event import EventDTO, Event, ExtendedEvent
from surveillance.gpio.Device import Device
from surveillance.gpio.MotionSensor import MotionSensor

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

m1 = MotionSensor(pin=1, websocket_manager=websocket_manager)
m2 = MotionSensor(pin=2, websocket_manager=websocket_manager)

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

@app.get("/devices")
def devices():
    return Device.device_list

@app.get("/events")
def events() -> List[EventDTO]:
    return ApiSubject.event_list


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    while True:
        print("interval")
        await websocket_manager.broadcast("test")
        await asyncio.sleep(3)