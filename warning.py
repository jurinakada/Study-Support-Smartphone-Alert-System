from study_mode import StudyMode
from LCD import LCD_messages

study = StudyMode()

def check_warning(study):
    if study.warning_level == 1:
        LCD_messages.warning_mes1()

    elif study.warning_level == 2:
        LCD_messages.warning_mes2()

    else:
        pass


# testing parts
if __name__ == "__main__":
    study = StudyMode()

    study.warning_level = 1
    check_warning(study)

    study.warning_level = 2
    check_warning(study)