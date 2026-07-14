import time
import LCD1602

#for testing
# try:
#     import LCD1602
# except ModuleNotFoundError:
#     import LCD1602_mock as LCD1602

from check_calendar import get_study_subjects


class LCD_messages:

    # The messages for starting
    @staticmethod
    def start_stu():
        LCD1602.init(0x3f, 1)

        LCD1602.write(0, 0, "Study Mode")
        LCD1602.write(0, 1, "is started")

        time.sleep(2)

        LCD1602.clear()
        LCD1602.write(0, 0, "Checking")
        LCD1602.write(0, 1, "Google Calendar")

        #display the subjects via google calender API
        LCD_messages.calenear_info()

    # The messages for finishing
    @staticmethod
    def finish_stu():
        LCD1602.clear()
        LCD1602.write(0, 0, "Study Mode")
        LCD1602.write(0, 1, "is stopped")

        time.sleep(2)

        LCD1602.clear()
        LCD1602.write(0, 0, "Summarizing")
        LCD1602.write(0, 1, "Final Report")

    # The messages for displaying calendar information via Google Calendar API
    @staticmethod
    def calendar_info():
        LCD1602.clear()
        LCD1602.write(0, 0, "Calendar info")
        LCD1602.write(0, 1, "will display")

        time.sleep(2)

        subjects = get_study_subjects()
        messages = []

        # If there are no subjects on Google Calendar
        if not subjects:
            messages.append("No study event")
            messages.append("today")
        else:
            messages.append("Today's study:")

            for subject in subjects:
                messages.append(subject)

        # Display messages on LCD
        for message in messages:
            LCD1602.clear()
            LCD1602.write(0, 0, message[:16])
            time.sleep(2)

        return subjects

    @staticmethod
    def warning_mes1():
        LCD1602.clear()
        LCD1602.write(0, 0, "Warning 1:")
        LCD1602.write(0, 1, "Phone detected")

        time.sleep(2)

        LCD1602.clear()
        LCD1602.write(0, 0, "Put it down")
        LCD1602.write(0, 1, "or buzzer ON")

    @staticmethod
    def warning_mes2():
        LCD1602.clear()
        LCD1602.write(0, 0, "Warning 2:")
        LCD1602.write(0, 1, "Buzzer ON")

        time.sleep(2)

        LCD1602.clear()
        LCD1602.write(0, 0, "Put your phone")
        LCD1602.write(0, 1, "down")