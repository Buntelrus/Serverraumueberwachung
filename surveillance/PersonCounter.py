from datetime import datetime, timedelta

from surveillance import WebSocketManager
from surveillance.Subject import Subject
from surveillance.dto.event import ExtendedEvent
from surveillance.gpio.MotionSensor import MotionSensor

TIME=1000
class PersonCounter(Subject):
    count: int = 0
    lastMotion = None
    def __init__(self, websocket_manager: WebSocketManager):
        self.websocket_manager = websocket_manager
        self.motionSensor1: MotionSensor = MotionSensor(4)
        self.motionSensor1.when_motion = lambda: self.analyseMotion(self.motionSensor1)
        # todo: change pin nr
        self.motionSensor2: MotionSensor = MotionSensor(666)
        self.motionSensor2.when_motion = lambda: self.analyseMotion(self.motionSensor2)

    def analyseMotion(self, sensor: MotionSensor):
        date = datetime.now()
        self.lastMotion.sensor = sensor
        self.lastMotion.date = date
        if (sensor == self.lastMotion.sensor):
            return
        if (self.lastMotion + timedelta(milliseconds=TIME) >= date):
            if (sensor == self.motionSensor1):
                self.count -= 1
                self.websocket_manager.broadcast(ExtendedEvent(
                    name='person-enter',
                    severity='info',
                ))
            else:
                self.count += 1
            self.notify(self.count)

