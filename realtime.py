import ntplib
import time
import threading

def getNetTime():
    c = ntplib.NTPClient()
    response = c.request('uk.pool.ntp.org', version=3)
    return response.tx_time

def getRealTime():
    global currentTime
    return time.ctime(currentTime)

class clock(threading.Thread):
    global currentTime
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global currentTime
        currentTime = getNetTime()
        while True:
            time.sleep(1)
            currentTime = currentTime+1

def startClock():
    global currentTime
    currentTime = 0
    cThread = clock(clock)
    cThread.start()
    while currentTime == 0:
        time.sleep(0.1)
