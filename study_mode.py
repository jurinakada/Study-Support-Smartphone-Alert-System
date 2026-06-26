import gpiozero
import time

from led_con import red_led_on, green_led
class StudyMode:
    def __init__(self):
        print('automatically setting (constract)');
        #flags
        is_running = False
        is_sitting = False
        #time
        start_time = None
        total_study_time = None
        study_time = None
        away_time = None

        #variables for detection
        is_detectd = False
        #warning variables
        warning_level = 0
        warning_count = 0
    def start_study():
        is_running = True
        start_time = 0

    def stop_study():

    def calculate():


