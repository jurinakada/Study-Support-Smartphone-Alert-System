import gpiozero
import time

from study_mode import StudyMode
from LCD import LCD_messages

from capture_control import Camera
from detection import detection

from led_control import LEDControl
from warning import check_warning
from buzzer_control import BuzzerControl
from discord_send import DiscordSend
from dht11_control import DHT11Control
from light_sensor import LightSensor
from final_report import create_final_report
from send_sheet import GoogleSheetsReport


btn = gpiozero.DigitalInputDevice(pin=16, pull_up=False)

study = StudyMode()
camera = None

#initialize each module
led_control = LEDControl(
    green_pin=5,
    red_pin=25
)

buzzer_control = BuzzerControl(pin=22)

discord = DiscordSend()

dht = DHT11Control(
    pin=14,
    interval=5
)

light = LightSensor(channel=0)


#environment data for final report
humidity = None
temperature = None
brightness = None

#time when sensors were last read
last_dht_time = 0
last_light_time = 0


try:
    while True:
        if btn.value == 1:
            #wait until the user releases the button
            while btn.value == 1:
                time.sleep(0.05)

            if study.is_running == False:
                study.start_study()
                print("Study mode is Started")

                #turn on the green LED
                led_control.check_led(study)

                #LCD display the message
                #Google Calendar information is also displayed
                LCD_messages.start_stu()

                #Open USB camera
                camera = Camera(camera_number=0)
                print("Camera opened")

                #read sensors immediately after starting
                last_dht_time = 0
                last_light_time = 0

            else:
                study.stop_study()
                print("Study Mode is Stopped")

                #turn off buzzer and LED
                buzzer_control.check_buzzer(study)
                led_control.check_led(study)

                #close the camera
                if camera is not None:
                    camera.close()
                    camera = None

                #final report will be summarized
                print("finalizing report")
                LCD_messages.finish_stu()

                final_report = create_final_report(
                    study,
                    brightness=brightness,
                    temperature=temperature,
                    humidity=humidity
                )

                print(final_report)

                #send final report to Discord
                discord.send_final_report(final_report)

                #send final report to Google Spreadsheet
                try:
                    sheet_report = GoogleSheetsReport(final_report)
                    sheet_report.send_report()

                except Exception as error:
                    print("Google Sheets Error:", error)

                break  #stop system

        if study.is_running == True:

            if camera is not None:
                print("Capturing frame...")
                frame = camera.capture_frame()

                if frame is not None:
                    print("Frame captured")
                    print("Running YOLO")

                    is_sitting, is_using_phone = detection(frame)

                    print("YOLO finished")
                    print("Sitting:", is_sitting)
                    print("Using phone:", is_using_phone)

                    if is_sitting == True:

                        if study.start_away_time is not None:
                            study.stop_away()
                            print("Away time measurement stopped")

                        study.is_sitting = True

                    else:
                        #start away time only once
                        if study.start_away_time is None:
                            study.start_away()
                            print("Away time measurement started")

                    #smartphone usage status
                    if is_using_phone == True:
                        #Start phone usage time only once
                        if study.start_phone_time is None:
                            study.start_phone_usage()
                            print("Phone usage measurement started")

                    else:
                        #stop using phone while measuring it
                        if study.start_phone_time is not None:
                            study.stop_phone_usage()
                            print("Phone usage measurement stopped")

            #save warning level before checking
            previous_warning_level = study.warning_level

            #check smartphone usage warning
            warning_level = check_warning(study)

            #send Discord message only when warning level changes
            if warning_level != previous_warning_level:

                if warning_level == 1:
                    discord.warning_notification(
                        "Smartphone usage has been detected"
                    )

                elif warning_level == 2:
                    discord.warning_notification(
                        "Please put your smartphone down"
                    )

            #control green and red LEDs
            led_control.check_led(study)

            #turn on buzzer when warning level is 2
            buzzer_control.check_buzzer(study)

            #measure temperature and humidity every 5 seconds
            if time.time() - last_dht_time >= dht.interval:
                try:
                    new_humidity, new_temperature = dht.read()

                    #save only valid data
                    if new_humidity is not None:
                        humidity = new_humidity
                        temperature = new_temperature

                except Exception as error:
                    print("DHT11 Error:", error)

                last_dht_time = time.time()

            #measure brightness every 5 seconds
            if time.time() - last_light_time >= 5:
                try:
                    brightness = light.read()
                    print("Brightness:", brightness)

                except Exception as error:
                    print("Light Sensor Error:", error)

                last_light_time = time.time()

        else:
            #turn off LED and buzzer while study mode is stopped
            led_control.check_led(study)
            buzzer_control.check_buzzer(study)

        time.sleep(0.1)


except KeyboardInterrupt:
    print("System was stopped by the user")

    if study.is_running == True:
        study.stop_study()


finally:
    #off the camera if it is still running
    if camera is not None:
        camera.close()

    #close GPIO modules
    buzzer_control.close()
    led_control.close()
    light.close()

    btn.close()
    print("Button was closed")