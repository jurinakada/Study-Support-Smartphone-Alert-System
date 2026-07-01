from study_mode import StudyMode
from LCD import LCD_messages

study = StudyMode()
message = LCD_messages()

if study.warning_level == 1:
    message.