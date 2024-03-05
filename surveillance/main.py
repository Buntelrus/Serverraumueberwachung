import asyncio
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI
from starlette.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware

from surveillance.ApiSubject import ApiSubject
from surveillance.PersonCounter import PersonCounter
from surveillance.WebSocketManager import WebSocketManager
from surveillance.dto.device import DeviceDTO
from surveillance.dto.event import EventDTO, ExtendedEvent
from surveillance.gpio.Device import Device
from surveillance.gpio.LED import LED
from surveillance.gpio.MotionSensor import MotionSensor

# async def printHello():
#     while True:
#         print("hello")
#         await asyncio.sleep(3)
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     loop = asyncio.get_event_loop()
#     asyncio.ensure_future(printHello(), loop=loop)
#     yield

# app = FastAPI(lifespan=lifespan)
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
p = PersonCounter(m1, m2, websocket_manager=websocket_manager)
led = LED(pin=3, websocket_manager=websocket_manager)

@app.get("/")
async def root():
    p.notify(ExtendedEvent(
        device=[p.motionSensor1.id, p.motionSensor2.id],
        data=p.count,
        name='person-enter',
        severity='info',
    ))
    led.on()
    led.off()
    return {"message": "Hello World"}

@app.get("/devices")
def devices() -> List[DeviceDTO]:
    return Device.device_list

@app.get("/events")
async def events() -> List[EventDTO]:
    return ApiSubject.event_list


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    while True:
        # keep the websocket alive!!!
        await asyncio.sleep(1000)