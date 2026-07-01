import gpiozero
import time

from led_con import red_led_on, green_led
class StudyMode:
    def __init__(self):
        print('automatically setting (constract)');
        #flags
        self.is_running = False
        self.is_sitting = False
        #time
        self.start_time = None
        self.total_study_time = None
        self.study_time = None
        self.away_time = None

        #variables for detection
        self.is_detectd = False
        #warning variables
        self.warning_level = 0
        self.warning_count = 0
    def start_study(self):
        self.is_running = True
        self.start_time = 0

    def stop_study(self):

    def get_current_study_time(self):
        if self.is_running == True:
            current_time = time.time()
            current_study_time = current_time - self.start_time
            return current_study_time
        else:
            return 0

    def get_total_studytime(self):
        if self.is_running == True:
            #get current time
            current_time = time.time()
            
            current_study_time = current_time - self.start_time
            
            return self.total_study_time + current_study_time
        else:
            return self.total_study_time
        


