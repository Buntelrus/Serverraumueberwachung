import asyncio

from surveillance.dto.device import TemperatureDTO
from surveillance.dto.event import Event
from surveillance.gpio.Device import Device

import adafruit_dht
import board

threshold = 1


class TemperatureSensor(Device):
    def __init__(self, **kwds):
        self.name = 'temperature'
        self.description = 'capture temperature and humidity'
        self.temperature = 0
        self.humidity = 0
        super().__init__(**kwds)
        # self.dht_device = adafruit_dht.DHT22(board.D4, use_pulseio=False)
        # asyncio.ensure_future(self.temperature_loop(), loop=asyncio.get_event_loop())

    async def temperature_loop(self):
        while True:
            try:
                temperature = self.dht_device.temperature
                humidity = self.dht_device.humidity

                print(f"{temperature}C°, Humidity: {humidity}")

                if self.temperature - threshold >= temperature >= self.temperature + threshold or self.humidity - threshold >= humidity >= self.humidity + threshold:
                    await self.websocket_manager.broadcast(Event(
                        device=self.id,
                        data=self.value
                    ))

                await asyncio.sleep(1)
            except:
                pass

    @property
    def value(self):
        return TemperatureDTO(
            temperature=self.temperature,
            humidity=self.humidity
        )
