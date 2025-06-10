import pyautogui
import time

print("You have 5 seconds to focus a text editor or input field...")
time.sleep(5)

print("Typing 'w', 'a', 's', 'd' with 1 second delay...")
for key in ['w', 'a', 's', 'd']:
    pyautogui.press(key)
    print(f"Pressed {key}")
    time.sleep(1)
print("Done!")
