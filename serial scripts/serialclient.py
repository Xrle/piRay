import RPi.GPIO as GPIO
import basetrans

def sync():
    latch =
    clock =
    data =
    response =
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(latch, GPIO.IN)
    GPIO.setup(clock, GPIO.IN)
    GPIO.setup(data, GPIO.IN)
    GPIO.setup(response, GPIO.OUT, initial=GPIO.LOW)
    binary = ""
    while GPIO.input(latch) == 0:
        pass
    while GPIO.input(latch) == 1:
        while GPIO.input(clock) == 0:
            pass
        binary.append(GPIO.input(data)
        GPIO.output(response, 1)
        while GPIO.input(clock) == 1:
            pass
        GPIO.output(reponse, 0)
    GPIO.output(response, 1)
    time = basetrans.bin2dec(int(binary))
    GPIO.output(response, 0)
    GPIO.cleanup()
    return time
    
