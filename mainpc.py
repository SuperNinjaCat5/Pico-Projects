import serial
import pydirectinput
import time
from rich import print
import threading

stop_event = threading.Event()

def move_mouse_right_continuous(stop_event):
    while not stop_event.is_set():
        pydirectinput.moveRel(5, 0)  # move 5 pixels instantly
        time.sleep(0.01)  # very short pause for smoothness


pydirectinput.PAUSE = 0

pico_port = "COM6"
baud_rate = 115200

print("[orange]Roblox, Minecraft, Retro[/orange]")
game = input()
game = game.lower()

def map_key_wasd_mc(line):
    if line == "Button Up tapped":
        return 'w'
    elif line == "Button Down tapped":
        return 'space'
    elif line == "Button Left tapped":
        return 'a'
    elif line == "Button Right tapped":
        return 'd'
    elif line == "Button Up held":
        return 'w'
    elif line == "Button Down held":
        return 'space'
    elif line == "Button Left held":
        return 'a'
    elif line == "Button Right held":
        return 'd'
    elif line == "Button Up released after hold":
        return 'w'
    elif line == "Button Down released after hold":
        return 'space'
    elif line == "Button Left released after hold":
        return 'a'
    elif line == "Button Right released after hold":
        return 'd'
    else:
        return "Failed To interpret check_good"

def map_key_wasd_retro(line):
    if line == "Button Up tapped":
        return 'w'
    elif line == "Button Down tapped":
        return 's'
    elif line == "Button Left tapped":
        return 'a'
    elif line == "Button Right tapped":
        return 'd'
    elif line == "Button Up held":
        return 'w'
    elif line == "Button Down held":
        return 's'
    elif line == "Button Left held":
        return 'a'
    elif line == "Button Right held":
        return 'd'
    elif line == "Button Up released after hold":
        return 'w'
    elif line == "Button Down released after hold":
        return 's'
    elif line == "Button Left released after hold":
        return 'a'
    elif line == "Button Right released after hold":
        return 'd'
    else:
        return "Failed To interpret check_good"
    
def map_key_wasd_roblox(line):
    if line == "Button Up tapped":
        return 'w'
    elif line == "Button Down tapped":
        return 's'
    elif line == "Button Left tapped":
        return 'a'
    elif line == "Button Right tapped":
        return 'd'
    elif line == "Button Up held":
        return 'w'
    elif line == "Button Down held":
        return 's'
    elif line == "Button Left held":
        return 'a'
    elif line == "Button Right held":
        return 'd'
    elif line == "Button Up released after hold":
        return 'w'
    elif line == "Button Down released after hold":
        return 's'
    elif line == "Button Left released after hold":
        return 'a'
    elif line == "Button Right released after hold":
        return 'd'
    else:
        return "Failed To interpret check_good"

def get_action(line):
    line = line.lower()
    print(f"DEBUG get_action input: {repr(line)}")
    if "released after hold" in line:
        return "released"
    elif "held" in line and "released" not in line:
        return "held"
    elif "tapped" in line:
        return "tapped"
    else:
        return "Failed to interpret get_action."


with serial.Serial(pico_port, baud_rate, timeout=1) as ser:
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        action = get_action(line)

        if game == "roblox":
            key = map_key_wasd_roblox(line)
            if action == "tapped":
                print(f"[yellow]Tap press: {key}[/yellow]")
                pydirectinput.keyDown(key)
                time.sleep(0.05)
                pydirectinput.keyUp(key)

            elif action == "held":
                print(f"[green]Hold start: {key}[/green]")
                pydirectinput.keyDown(key)

            elif action == "released":
                print(f"[green]Hold end: {key}[/green]")
                pydirectinput.keyUp(key)

            else:
                print(f"[red]Unknown action from line: {action}[/red]")

        elif game == "minecraft":
            key = map_key_wasd_mc(line)
            if key in ("a", "d") and action == "tapped":
                if key == "a":
                    pydirectinput.moveRel(-50, 0, duration=0.1)
                if key == "d":
                    pydirectinput.moveRel(50, 0, duration=0.1)
                elif action == "held" and key == "a":
                    move_thread = threading.Thread(target=move_mouse_right_continuous, daemon=True)
                    move_thread.start()
                elif action == "held" and key == "d":
                    move_thread = threading.Thread(target=move_mouse_right_continuous, daemon=True)
                    move_thread.start()
                elif action == "released":
                    stop_event.set()
                    move_thread.join()

            else:
                if action == "tapped":
                    print(f"[yellow]Tap press: {key}[/yellow]")
                    pydirectinput.keyDown(key)
                    time.sleep(0.05)
                    pydirectinput.keyUp(key)

                elif action == "held":
                    pydirectinput.keyDown("ctrl")
                    print(f"[green]Hold start: {key}[/green]")
                    pydirectinput.keyDown(key)

                elif action == "released":
                    print(f"[green]Hold end: {key}[/green]")
                    pydirectinput.keyUp(key)

                else:
                    print(f"[red]Unknown action from line: {action}[/red]")
  
        elif game == "retro":
            key = map_key_wasd_retro(line)
            if action == "tapped":
                print(f"[yellow]Tap press: {key}[/yellow]")
                pydirectinput.keyDown(key)
                time.sleep(0.05)
                pydirectinput.keyUp(key)

            elif action == "held":
                print(f"[green]Hold start: {key}[/green]")
                pydirectinput.keyDown(key)

            elif action == "released":
                print(f"[green]Hold end: {key}[/green]")
                pydirectinput.keyUp(key)

            else:
                print(f"[red]Unknown action from line: {action}[/red]")


