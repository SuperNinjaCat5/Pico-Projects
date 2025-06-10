from machine import Pin  # type: ignore
import time

HOLD_THRESHOLD = 500

buttons = {
    "Right": Pin(15, Pin.IN, Pin.PULL_UP),
    "Up": Pin(14, Pin.IN, Pin.PULL_UP),
    "Left": Pin(13, Pin.IN, Pin.PULL_UP),
    "Down": Pin(29, Pin.IN, Pin.PULL_UP)
}

last_states = {n: True for n in buttons}
press_start_times = {n: 0 for n in buttons}
button_held_flags = {n: False for n in buttons}

while True:
    now = time.ticks_ms()
    for name, pin in buttons.items():
        state = pin.value()

        if not state and last_states[name]:
            press_start_times[name] = now
            button_held_flags[name] = False

        elif not state and not last_states[name]:
            if not button_held_flags[name] and time.ticks_diff(now, press_start_times[name]) >= HOLD_THRESHOLD:
                print("Button", name, "held")
                button_held_flags[name] = True

        elif state and not last_states[name]:
            if time.ticks_diff(now, press_start_times[name]) < HOLD_THRESHOLD:
                print("Button", name, "tapped")
            else:
                if button_held_flags[name]:
                    print("Button", name, "released after hold")

        last_states[name] = state

    time.sleep(0.05)
