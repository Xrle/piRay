import RPi.GPIO as GPIO
import basetrans, realtime

def sync():
    latch =
    clock =
    data =
    response =
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(latch, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clock, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(data, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(response, GPIO.IN)
    time = realtime.getNetTime()
    binary = str(basetrans.dec2bin(int(time)))
    GPIO.output(latch, 1)
    for i in binary:
        GPIO.output(data, int(i))
        GPIO.output(clock, 1)
        while GPIO.input(response) == 0:
            pass
        GPIO.output(clock, 0)
    GPIO.output(latch, 0)
    while GPIO.input(response) == 0:
        pass
    GPIO.cleanup()
    
    
