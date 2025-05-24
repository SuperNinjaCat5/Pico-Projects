from machine import Pin # type: ignore
import time

def toggle(var):
    return not var

led = Pin(15, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)
buttononoff = False

while True:
    if button.value() == 0: 
        print("Is pressed")
        buttononoff = toggle(buttononoff)
        time.sleep(0.1)
    else:
        print("Not pressed")
    
    if buttononoff == True:
        led.value(1)
    elif buttononoff == False:
        led.value(0)
    time.sleep(0.1)
