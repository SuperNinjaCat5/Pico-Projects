from machine import Pin # type: ignore
import time

def toggle(var):
    return not var

button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0: 
        print("Is pressed")
        time.sleep(0.1)
    else:
        print("Not pressed")