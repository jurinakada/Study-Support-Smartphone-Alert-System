import gpiozero
import time

from study_mode import StudyMode
from LCD import LCD_messages


btn  = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
try:
    while True:
        if btn.value == 1:
            #wait until the user releases the button
            while btn.value == 1:
                  time.sleep(0.05)

            if study.is_running == False:
                study.start_study()
                print("Study mode is Started")
                #LCD display the message
                LCD_messages.start_stu()

            else:
                study.stop_study()
                print("Study Mode is Stopped")

                #final report will be summrized
                print("finalizing report")
                LCD_messages.finish_stu()
                break #stop system
        time.sleep(0.1)
except KeyboardInterrupt:
    print("System was stopped by the user")

finally:
    btn.close()
    print("Button was closed")