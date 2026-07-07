from study_mode import StudyMode

btn  = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
try:
    while True:
        if btn.value == 1:
            if study.is_running == False:
                study.start_study()
                print("Study mode is Started")
            else:
                study.stop_study()
                print("Study Mode is Stopped")
                #final report will be summrized
                print("finalizing report")
                break #stop system
        time.sleep(1)
    time.sleep(1)
except KeyboardInterrupt:
    btn.close()