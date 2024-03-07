from datetime import datetime, timedelta

from surveillance.gpio.Device import Device
from surveillance.gpio.MotionSensor import MotionSensor

TIME=1000
class PersonCounter(Device):
    def __init__(self, motionSensor1: MotionSensor, motionSensor2: MotionSensor, **kwargs):
        self.name = 'person-counter'
        self.description = 'Count the person which enter the server room'
        self.value: int = 0
        self.lastMotion = None
        self.motionSensor1: MotionSensor = motionSensor1
        self.motionSensor1.when_motion = lambda: (
            self.motionSensor1.when_motion(),
            self.analyseMotion(self.motionSensor1)
        )
        self.motionSensor2: MotionSensor = motionSensor2
        self.motionSensor2.when_motion = lambda: (
            self.motionSensor2.when_motion(),
            self.analyseMotion(self.motionSensor2)
        )
        super().__init__(**kwargs)

    def analyseMotion(self, sensor: MotionSensor):
        date = datetime.now()
        self.lastMotion.sensor = sensor
        self.lastMotion.date = date
        if sensor == self.lastMotion.sensor:
            return
        if self.lastMotion + timedelta(milliseconds=TIME) >= date:
            if sensor == self.motionSensor1:
                self.value -= 1
            else:
                self.value += 1

            self.notify(self.value)

