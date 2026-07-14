import gpiozero
import time


class LEDControl:
    def __init__(self, green_pin=5, red_pin=25):
        self.led_green = gpiozero.DigitalOutputDevice(pin=green_pin)
        self.led_red = gpiozero.DigitalOutputDevice(pin=red_pin)

        # Warning level 1 flashing control
        self.last_blink_time = time.time()
        self.red_led_state = False

    def check_led(self, study):
        # Green LED: ON while study mode is running
        if study.is_running == True:
            self.led_green.on()
        else:
            self.led_green.off()

        # Warning level 2: Red LED stays ON
        if study.warning_level == 2:
            self.led_red.on()
            self.red_led_state = True

        # Warning level 1: Red LED flashes every 1 second
        elif study.warning_level == 1:
            current_time = time.time()

            if current_time - self.last_blink_time >= 1:
                self.red_led_state = not self.red_led_state

                if self.red_led_state == True:
                    self.led_red.on()
                else:
                    self.led_red.off()

                self.last_blink_time = current_time

        # No warning: Red LED OFF
        else:
            self.led_red.off()
            self.red_led_state = False

    def close(self):
        self.led_green.off()
        self.led_red.off()

        self.led_green.close()
        self.led_red.close()


