from gpiozero

class LCD_messages:
    #The messages for starting
    def start_stu():

        LCD1602.init(0x3f, 1)

        LCD1602.write(0,0 'Study Mode is started')

        LCD1602.write(1,0 'Checking your schedules from your google calender')

        
    #The messages for finishing
    def finish_stu():

        LCD1602.write(0,0 'Study Mode is stopped')
        lCD1602.write(1,0 'Summrizing the Final Report')
    
    #The messages for displaying calender information via Google Calender API
    def calender_info():
    
        LCD1602.write(0,0 'The calender information will be dispalyed')
    
    def warning_mes1 ()
        LCD1602.write(0,0 'Warning 1: Smartphone use detected')

        LCD1602.write(0,0 'Please put it down, or the warning buzzer will sound.')

    def warning_mes2 ()

       LCD1602.write(0,0 'Warning 2: Smartphone use detected')

       LCD1602.write(0,0 'The buzzer is turned on. Please put your phone down.')

