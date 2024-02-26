from surveillance.Subject import Subject
from surveillance.gpio.MotionSensor import MotionSensor

TIME=1000
class PersonCounter(Subject):
    count: int = 0
    lastMotion = None
    def __init__(self):
        self.motionSensor1: MotionSensor = MotionSensor(4)
        self.subscribe()
        # todo: change pin nr
        self.motionSensor2: MotionSensor = MotionSensor(666)
        self.subscribe()

    def analyseMotion(self, sensor: MotionSensor):
        date =
        if ():
        self.lastMotion.sensor = sensor

