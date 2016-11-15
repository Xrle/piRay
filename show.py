from sense_hat import AstroPi
import time
ap = AstroPi()

def draw(rate,subtracted):
        ap.show_message(str(rate), scroll_speed=1, text_colour=[255,0,0]) # red for count rate
        ap.show_message(str(subtracted), scroll_speed=1, text_colour=[0,0,255]) #blue for faulty/noisy pixels

def calibrateMessage():
        ap.show_letter("C")

def running():
        ap.show_letter("R")

def detected():
        ap.show_letter("D")
        
        
