#coding: utf-8
import gpiozero
import time


class BuzzerControl:
    def __init__(self, pin=22):
        self.buzzer = gpiozero.DigitalOutputDevice(pin=pin) #GPIO 22

    def check_buzzer(self, study):
        if study.warning_level == 2:
            self.buzzer.on()

        else:
            self.buzzer.off()

    def close(self):
        self.buzzer.off()
        self.buzzer.close()


#testing parts
if __name__ == "__main__":
    from study_mode import StudyMode

    study = StudyMode()
    buzzer_control = BuzzerControl(pin=22)

    try:
        while True:
            study.warning_level = 2
            buzzer_control.check_buzzer(study)
            print("Buzzer ON")

            time.sleep(3)

            study.warning_level = 0
            buzzer_control.check_buzzer(study)
            print("Buzzer OFF")

            time.sleep(3)

            # print("Piezo Buzzer ON")
            # buzzer.on()
            # time.sleep(1)

            # print("Piezo BUzzer OFF")
            # buzzer.off()
            # time.sleep(1)

    except KeyboardInterrupt:
        print("Buzzer test was stopped")

    finally:
        buzzer_control.close()