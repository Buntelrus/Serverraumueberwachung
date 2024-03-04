from surveillance.ApiSubject import ApiSubject
from gpiozero import MotionSensor as ZeroMotionSensor

from surveillance.dto.event import ExtendedEvent
from surveillance.gpio.Device import Device


class MotionSensor(Device, ApiSubject):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        # self.sensor: ZeroMotionSensor = ZeroMotionSensor(self.pin)
        self.sensor = f"sensor with pin: {self.pin}"
        # self.motionDetected: bool = self.sensor.value
        # self.sensor.when_motion = lambda: self.updateState(True)
        # self.sensor.when_no_motion = lambda: self.updateState(False)

    # only notify when state has changed
    def updateState(self, newState: bool):
        self.notify(newState)
        self.websocket_manager.broadcast()

