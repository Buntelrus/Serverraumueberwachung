from surveillance.Subject import Subject
from gpiozero import MotionSensor

class MotionSensor(Subject):
    def __init__(self, pin: str):
        self.sensor: MotionSensor = MotionSensor(pin)
        self.motionDetected: bool = self.sensor.value
        self.sensor.when_motion = lambda: self.updateState(True)
        self.sensor.when_no_motion = lambda: self.updateState(False)

    # only notify when state has changed
    def updateState(self, newState: bool):
        self.notify(newState)

