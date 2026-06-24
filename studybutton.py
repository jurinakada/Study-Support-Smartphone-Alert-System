


from study_mode import StudyMode

btn  = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
try:
    while True:
        if btn.value == 1:
            print("the Study mode is started")
            if study.is_running == False:
                study.start()
            else:
                study.stop()
            time.sleep(1)
    time.sleep(1)
except KeyboardInterrupt:
    btn.close()