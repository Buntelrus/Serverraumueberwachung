from gpiozero import LED as ZeroLED

from surveillance.gpio.Device import Device


class LED(ZeroLED, Device):
# class LED(Device):
    def __init__(self, **kwds):
        self.name = 'led'
        self.description = 'A simple LED'
        pin = kwds.get('pin')
        ZeroLED.__init__(pin)
        Device.__init__(**kwds)

    def on(self):
        super().on()
        self.notify(True)

    def off(self):
        super().off()
        self.notify(False)

