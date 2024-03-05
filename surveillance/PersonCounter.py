from datetime import datetime, timedelta

from surveillance.ApiSubject import ApiSubject
from surveillance.dto.event import ExtendedEvent
from surveillance.gpio.MotionSensor import MotionSensor

TIME=1000
class PersonCounter(ApiSubject):
    count: int = 0
    lastMotion = None
    def __init__(self, motionSensor1: MotionSensor, motionSensor2: MotionSensor, **kwargs):
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
                self.count -= 1
            else:
                self.count += 1

            self.notify(ExtendedEvent(
                    device=[self.motionSensor1.id, self.motionSensor2.id],
                    data=self.count,
                    name='person-enter',
                    severity='info',
            ))

