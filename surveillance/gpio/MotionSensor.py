from gpiozero import MotionSensor as ZeroMotionSensor

from surveillance.gpio.Device import Device


class MotionSensor(Device):
    def __init__(self, **kwds):
        self.name = 'motion'
        self.description = 'Sensor can detect motion'
        super().__init__(**kwds)
        # self.sensor: ZeroMotionSensor = ZeroMotionSensor(self.pin)
        self.sensor = f"sensor with pin: {self.pin}"
        # self.motionDetected: bool = self.sensor.value
        # self.sensor.when_motion = lambda: self.updateState(True)
        # self.sensor.when_no_motion = lambda: self.updateState(False)

    # only notify when state has changed
    def updateState(self, newState: bool):
        if (self.motionDetected != newState):
            self.notify(newState)

