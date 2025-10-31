import pydirectinput
import time
import keyboard
import threading

# Configuration
pydirectinput.PAUSE = 0
KEY_SEQUENCE = ["6", "7", "8", "9"] * 10 + ["mouse_click"]
PER_KEY_HOLD = 0.02
TOGGLE_KEY = "q"
EXIT_KEY = "2"

is_running = False


def auto_press():
    global is_running
    while True:
        if is_running:
            for key in KEY_SEQUENCE:
                if key == "mouse_click":
                    pydirectinput.mouseDown()
                    time.sleep(PER_KEY_HOLD)
                    pydirectinput.mouseUp()
                else:
                    pydirectinput.keyDown(key)
                    time.sleep(PER_KEY_HOLD)
                    pydirectinput.keyUp(key)
        time.sleep(PER_KEY_HOLD)


def handle_toggle_key(event):
    global is_running
    is_running = not is_running
    print("running" if is_running else "stopped")


keyboard.on_press_key(TOGGLE_KEY, handle_toggle_key)

if __name__ == "__main__":
    auto_press_thread = threading.Thread(target=auto_press, daemon=True)
    auto_press_thread.start()
    print(f"Press '{TOGGLE_KEY}' to Start/Stop. Press '{EXIT_KEY}' to close.")
    keyboard.wait(EXIT_KEY)
    print("\nClosing Program...")
