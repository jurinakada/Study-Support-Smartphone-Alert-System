#coding: utf-8
import gpiozero
import time

buzzer = gpiozero.DigitalOutputDevice(pin=22) #GPIO 22
try:
    while True:
        print("Piezo Buzzer ON")
        buzzer.on()
        time.sleep(1)

        print("Piezo BUzzer OFF")
        buzzer.off()
        time.sleep(1)

except KeyboardInterrupt:
    buzzer.close()
