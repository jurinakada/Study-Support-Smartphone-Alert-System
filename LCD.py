from gpiozero

def setup():
    LCD1602.init(0x3f, 1)
    lCD1602.write(0,0 'Study mode is started')
    lCD1602.write(1,0 'Checking your schedules from your google calender')
