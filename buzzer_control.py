#coding: utf-8
import gpiozero
import time
from study_mode import StudyMode

study = StudyMode()
buzzer = gpiozero.DigitalOutputDevice(pin=22) #GPIO 22
try:
    while True:
        if study.warning_level == 2:
            buzzer.on()
            time.sleep(1)
        else:
            buzzer.off()
            time.sleep(1)

        # print("Piezo Buzzer ON")
        # buzzer.on()
        # time.sleep(1)

        # print("Piezo BUzzer OFF")
        # buzzer.off()
        # time.sleep(1)

except KeyboardInterrupt:
    buzzer.close()
