import gpiozero
import time

from study_mode import StudyMode
from LCD import LCD_messages

from camera import Camera
from detection import detection

btn  = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
camera = None

try:
    while True:
        if btn.value == 1:
            #wait until the user releases the button
            while btn.value == 1:
                  time.sleep(0.05)

            if study.is_running == False:
                study.start_study()
                print("Study mode is Started")
                #LCD display the message
                LCD_messages.start_stu()

                # Open USB camera
                camera = Camera(camera_number=0)

            else:
                study.stop_study()
                print("Study Mode is Stopped")
                
                #close the camera
                if camera is not None:
                    camera.close()
                    camera = None

                #final report will be summarized
                print("finalizing report")
                LCD_messages.finish_stu()
                break #stop system

        if study.is_running == True and camera is not None:
            frame = camera.capture_frame()

            if frame is not None:
                is_sitting, is_using_phone = detection(frame)

                print("Sitting:", is_sitting)
                print("Using phone:", is_using_phone)

                if is_sitting == True:

                    if study.start_away_time is not None:
                        study.stop_away()
                        print("Away time measurement stopped")

                    study.is_sitting = True
            
                else:
                    #stat away time only once
                    if study.start_away_time is None:
                        study.start_away()
                        print("Away time measurement started")

                #smartphone usage status
                if is_using_phone == True:
                    # Start phone usage time only once
                    if study.start_phone_time is None:
                        study.start_phone_usage()
                        print("Phone usage measurement started")

                else:
                    #stop using phone while measuring it
                    if study.start_phone_time is not None:
                        study.stop_phone_usage()
                        print("Phone usage measurement stopped")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("System was stopped by the user")

    if study.is_running == True:
        study.stop_study()

finally:
    #off the camera if it is still running
    if camera is not None:
        camera.close()
        
    btn.close()
    print("Button was closed")