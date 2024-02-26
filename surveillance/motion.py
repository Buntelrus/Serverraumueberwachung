from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(4)
led = LED(17)

pir.when_motion = lambda: print("motion detected")
pir.when_no_motion = lambda: print("no motion detected")

pause()
