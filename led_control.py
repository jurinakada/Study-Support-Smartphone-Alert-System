import gpiozero
import time

study = StudyMode()
led_green = gpiozero.DigitalOutputDevice(pin=5) #GPIO = 5
led_red = gpiozero.DigitalOutputDevices(pin=25) #GPIO = 25

try:
    while True:
        # turn  on the green LED
        led_green.on()
        
        #detection system detected  smartphone usage
        if is_detected == True:
            led_red.on()

        #when the warning level becomes 1
        if study.warning_level == 1:
            while True:
                led_red.on ()
                time.sleep(1)
        


except KeyboardInterrupt:
    led_green.close()
    led_green.close()


