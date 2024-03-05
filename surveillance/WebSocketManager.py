from starlette.websockets import WebSocket, WebSocketDisconnect
from typing_extensions import Any


class WebSocketManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_json(self, message: Any, websocket: WebSocket):
        try:
            await websocket.send_json(message)
        except WebSocketDisconnect:
            self.disconnect(websocket)


    async def broadcast(self, message: Any):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except WebSocketDisconnect:
                self.disconnect(connection)