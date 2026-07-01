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
    
        lCD1602.write(0,0 'The calender infromation will be dispalyed')

