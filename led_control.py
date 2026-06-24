import gpiozero
import time

study = StudyMode()
led_green = gpiozero.DigitalOutputDevice(pin=5) #GPIO = 5
led_red = gpiozero.DigitalOutputDevices(pin=25) #GPIO = 25

try:
    while True:
        # turn  on the green LED
        led_green.on()
        
        #detection system detected  smartphone usages

        #when the warning level becomes 1
        if study.warning_level == 1:
            led_red.on()
        


except KeyboardInterrupt:
    led_green.close()
    led_green.close()


