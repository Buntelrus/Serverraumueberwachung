from gpiozero import LED as ZeroLED

from surveillance.gpio.Device import Device


class LED(Device, ZeroLED):
# class LED(Device):
    def __init__(self, **kwds):
        self.name = 'led'
        self.description = 'A simple LED'
        self.value = False
        super().__init__(**kwds)

    def on(self):
        super().on()
        self.notify(True)

    def off(self):
        super().off()
        self.notify(False)

