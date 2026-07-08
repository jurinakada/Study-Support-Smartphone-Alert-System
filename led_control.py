import gpiozero
import time
from study_mode import StudyMode

study = StudyMode()
led_green = gpiozero.DigitalOutputDevice(pin=5) #GPIO = 5
led_red = gpiozero.DigitalOutputDevices(pin=25) #GPIO = 25

try:
    while True:
        # turn  on the green LED
        led_green.on()
        
        #turn off the green LED when study mode is off
        if study.is_running == False:
            led_green.off()
            led_green.close()
            led_red.close()
        else:
            pass
        #detection system detected  smartphone usage
        if study.is_detected == True:
            led_red.on()

            #when the warning level becomes 1
            if study.warning_level == 1:
                while True:
                    led_red.on()
                    time.sleep(1)
                    led_red.off()
                    time.sleep(1)
        elif study.is_detected == False:
            led_red.off()
            
        


c
    led_green.close()
    led_red.close()


