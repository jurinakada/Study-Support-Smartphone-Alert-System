from study_mode import StudyMode
from LCD import LCD_messages

btn  = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
try:
    while True:
        if btn.value == 1:
            if study.is_running == False:
                study.start_study()
                print("Study mode is Started")
                #LCD display the message
                start_stu()

            else:
                study.stop_study()
                print("Study Mode is Stopped")

                #final report will be summrized
                print("finalizing report")
                finish_stu()
                break #stop system
        time.sleep(1)
    time.sleep(1)
except KeyboardInterrupt:
    btn.close()