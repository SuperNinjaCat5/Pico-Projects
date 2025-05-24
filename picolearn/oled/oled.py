from machine import Pin, I2C
from micropython import const
import picolearn.oled.sh1106 as sh1106
import time
import picolearn.oled.utilts as utilts

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = sh1106.SH1106_I2C(128, 64, i2c)

oled.fill(0)
oled.text("Hello", 0, 0)
oled.show()

#utilts.checkforbuttonpress(14) #debug

button = Pin(14, Pin.IN, Pin.PULL_UP)

print("Waiting for button press to keep going...")
oled.fill(0)
oled.text("Waiting for", 0, 0)
oled.text("button press", 0, 10)
oled.text("to keep", 0, 20)
oled.text("going...", 0, 30)
oled.show()

while button.value() == 1:
    time.sleep_ms(50) 

timer = 60

while True:
    timer -= 1
    print(timer)
    oled.fill(0)
    oled.text(f"{timer}", 0, 0)
    oled.show()
    time.sleep(1)
    if timer == 0:
        break

print("Waiting for button press to keep going...")
oled.fill(0)
oled.text("Waiting for", 0, 0)
oled.text("button press", 0, 10)
oled.text("to keep", 0, 20)
oled.text("going...", 0, 30)
oled.show()

while button.value() == 1:
    time.sleep_ms(50) 

oled.poweroff()
print("Display turned off.")
