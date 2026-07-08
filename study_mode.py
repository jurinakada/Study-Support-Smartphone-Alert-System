import time


class StudyMode:
    def __init__(self):
        # flags
        self.is_running = False
        self.is_sitting = False

        # time (recording)
        self.start_time = None  # the variable for recording time when the user starts studying
        self.stop_time = None  # the variable for recording time when the user stops studying
        self.start_away_time = None  # When the user is away from the desk for any reasons, away time is being measured
        self.stop_away_time = None  # When the user come back on the desk, away time is stopped
        self.current_time = None  # variable for current time
        self.study_time = 0  # total studytime including away time
        self.away_time = 0  # total awaytime
        self.actual_study_time = 0  # actual total study time (= study_time - away_time)

        # variables for detection
        self.is_detected = False

        # warning variables
        self.warning_level = 0  # range 0-1
        self.warning_count = 0  # total number of warning the user gets

    def start_study(self):
        self.is_running = True
        self.start_time = time.time()
        self.stop_time = None

        self.study_time = 0
        self.away_time = 0
        self.actual_study_time = 0

    def stop_study(self):
        if self.is_running == True:
            self.stop_time = time.time()

            self.study_time = self.stop_time - self.start_time
            self.actual_study_time = self.study_time - self.away_time

            self.is_running = False

    def get_current_time(self):
        self.current_time = time.time()
        return self.current_time

    def get_total_study_time(self):
        if self.is_running == True:
            self.study_time = time.time() - self.start_time

        return self.study_time

    def start_away(self):
        if self.is_running == True and self.is_sitting == True:
            self.is_sitting == False
            self.start_away_time = time.time()

    def stop_away(self):
        if self.is_running == True and self.is_sitting == False:
            self.is_sitting == True
            self.stop_away_time = time.time()

            self.away_time += self.stop_away_time - self.start_away_time

            self.start_away_time = None
            self.stop_away_time = None

    def get_total_away_time(self):
        total_away_time = self.away_time

        if self.start_away_time is not None:
            total_away_time += time.time() - self.start_away_time

        return total_away_time

    def get_actual_study_time(self):
        total_study_time = self.get_total_study_time()
        total_away_time = self.get_total_away_time()

        self.actual_study_time = total_study_time - total_away_time
        return self.actual_study_time


# testing parts
# if __name__ == "__main__":
#     study = StudyMode()

#     print("Study mode test started")

#     study.start_study()
#     print("Start study")

#     time.sleep(3)
#     print("Total study time:", study.get_total_study_time())

#     study.start_away()
#     print("Away started")

#     time.sleep(2)
#     print("Total away time:", study.get_total_away_time())
#     print("Actual study time:", study.get_actual_study_time())

#     study.stop_away()
#     print("Away stopped")

#     time.sleep(3)

#     study.stop_study()
#     print("Study stopped")

#     print("--------------- Final Result ---------------")
#     print("Total study time:", study.get_total_study_time())
#     print("Total away time:", study.get_total_away_time())
#     print("Actual study time:", study.get_actual_study_time())
#     print("Warning count:", study.warning_count)