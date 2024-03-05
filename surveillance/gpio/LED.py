from gpiozero import LED as ZeroLED

from surveillance.gpio.Device import Device


class LED(Device, ZeroLED):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.name = 'led'

    def on(self):
        self.notify(True)

    def off(self):
        self.notify(False)

