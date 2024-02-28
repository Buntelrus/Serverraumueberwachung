from surveillance.Subject import Subject
from gpiozero import MotionSensor

from surveillance.WebSocketManager import WebSocketManager
from surveillance.gpio.Actor import Actor


class MotionSensor(Subject, Actor):
    def __init__(self, pin: str, websocket_manager: WebSocketManager):
        self.sensor: MotionSensor = MotionSensor(pin)
        self.motionDetected: bool = self.sensor.value
        self.websocket_manager: WebSocketManager = websocket_manager
        self.sensor.when_motion = lambda: self.updateState(True)
        self.sensor.when_no_motion = lambda: self.updateState(False)

    # only notify when state has changed
    def updateState(self, newState: bool):
        self.notify(newState)
        self.websocket_manager.broadcast()

