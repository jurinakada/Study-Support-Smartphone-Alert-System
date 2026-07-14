
#light sensor

from gpiozero import MCP3008
from time import sleep


class LightSensor:
    def __init__(self, channel=0):
        # read MCP3008 CH0
        self.light_sensor = MCP3008(channel=channel)

    def read(self):
        #read the value (0.0 - 1.0)
        brightness = self.light_sensor.value

        #check the brightness whether it's bright or dark
        if brightness >= 0.5:
            print("Bright")

        else:
            print("Dark")

        return brightness

    def close(self):
        self.light_sensor.close()


#testing parts
if __name__ == "__main__":
    light = LightSensor(channel=0)

    try:
        while True:
            brightness = light.read()
            print("Brightness:", brightness)

            sleep(1)

    except KeyboardInterrupt:
        print("Light sensor measurement stopped")

    finally:
        light.close()










# #light sensor

# from gpiozero import MCP3008
# from time import sleep

# # read MCP3008 CH0

# light_sensor = MCP3008(channel=0)

# try:
#     while True:
#         #read the value (0.0 - 1.0)
#         brightness = light_sensor.value

#         #check the brightness whether it's bright or dark
#         if brightness >= 0.5:
#             print("Bright")

#         else:
#             print("Dark")

#         sleep(1)
# except KeyboardInterrupt:
#     light_sensor.close()