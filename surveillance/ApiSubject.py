from surveillance.Subject import Subject, SubscriptionArguments
from surveillance.WebSocketManager import WebSocketManager


class ApiSubject(Subject):
    websocket_manager: WebSocketManager
    def __init__(self, websocket_manager: WebSocketManager, **kwds):
        self.websocket_manager = websocket_manager
        super().__init__(**kwds)

    def notify(self, payload: SubscriptionArguments):
        super().notify(payload)
        self.websocket_manager.broadcast(payload)
