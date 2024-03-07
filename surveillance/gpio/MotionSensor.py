from gpiozero import MotionSensor as ZeroMotionSensor

from surveillance.gpio.Device import Device


class MotionSensor(Device):
    def __init__(self, pin: int, **kwds):
        self.name = 'motion'
        self.description = 'Sensor can detect motion'
        self.value: bool = False
        self.sensor: ZeroMotionSensor = ZeroMotionSensor(pin)
        self.value: bool = self.sensor.value
        super().__init__(pin=pin, **kwds)
        # self.sensor = f"sensor with pin: {self.pin}"
        self.sensor.when_motion = lambda: self.updateState(True)
        self.sensor.when_no_motion = lambda: self.updateState(False)

    # only notify when state has changed
    def updateState(self, newState: bool):
        if (self.value != newState):
            self.notify(newState)

