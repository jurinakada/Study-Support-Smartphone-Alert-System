from study_mode import StudyMode
from LCD import LCD_messages

import time

study = StudyMode()

def check_warning(study, threshold1 = 60, threshold2 = 120):
    #get the current countinuous user's smartphone usage time

    phone_usage_time = study.get_current_phone_usage_time()

    #save the previous warning level
    
    previous_warning_level = study.warning_level

    #if the user doesn't use samrtphone, warning level 0
    if study.is_using_phone == False:
        study.warning_level = 0

    #warning level 2
    elif phone_usage_time >= threshold2:
        study.warning_level = 2

    #warning level 1
    elif phone_usage_time >= threshold1:
        study.warning_level = 1

    else:
        study.warning_level = 0
    
    #when the warning level changes, display messages and count the warning.
    if study.warning_level != previous_warning_level:

        if study.warning_level == 1:
            LCD_messages.warning_mes1()
            study.warning_count += 1

        elif study.warning_level == 2:
            LCD_messages.warning_mes2()
            study.warning_count += 1
    #when the warning level becomes 0, just return study.warning_level
    return study.warning_level

    # testing parts
if __name__ == "__main__":
    study = StudyMode()

    study.start_study()
    study.start_phone_usage()

    #thresholds are shortened for testing
    while study.get_current_phone_usage_time() < 6:
        check_warning(
            study,
            threshold1=2,
            threshold2=4
        )

    study.stop_phone_usage()
    study.stop_study()

    print("Warning count:", study.warning_count)













# def check_warning(study):
#     if study.warning_level == 1:
#         LCD_messages.warning_mes1()

#     elif study.warning_level == 2:
#         LCD_messages.warning_mes2()

#     else:
#         pass


# # testing parts
# if __name__ == "__main__":
#     study = StudyMode()

#     study.warning_level = 1
#     check_warning(study)

#     study.warning_level = 2
#     check_warning(study)