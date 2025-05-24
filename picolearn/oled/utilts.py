from machine import Pin
import time

def checkforbuttonpress(pin):

    button = Pin(pin, Pin.IN, Pin.PULL_UP)  # Button on GPIO14, active low
    
    print("Waiting for button press...")

    while button.value() == 1:  # Loop until button pressed (value goes LOW)
            time.sleep_ms(50)       # Small delay to avoid busy waiting

    print("Button pressed!")
