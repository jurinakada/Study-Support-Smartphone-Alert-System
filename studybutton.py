from study_mode import StudyMode

btn  = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
try:
    while True:
        if btn.value == 1:
            print("Study mode is Started")
            if study.is_running == False:
                study.start()
            else:
                study.stop()
            time.sleep(1)
            if study.is_running == True:
                if btn.value == 1:
                    study.start()
                    print("Study Mode is Stopped")
                    time.sleep(1)
    time.sleep(1)
except KeyboardInterrupt:
    btn.close()