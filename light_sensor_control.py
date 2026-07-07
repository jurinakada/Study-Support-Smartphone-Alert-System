#light sensor

from gpiozero import MCP3008
from time import sleep

# read MCP3008 CH0

light_sensor = MCP3008(channel=0)

try:
    while True:
        #read the value (0.0 - 1.0)
        brightness = light_sensor.value

        #check the brightness whether it's bright or dark
        if brightness >= 0.5:
            print("Bright")

        else:
            print("Dark")

        sleep(1)
except KeyboardInterrupt:
    light_sensor.close()