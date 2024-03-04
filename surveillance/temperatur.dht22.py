import time

import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        print(f"{temperature}C°, Humidity: {humidity}")
        time.sleep(1)
    except:
        print("error!")