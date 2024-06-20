import pyautogui
import keyboard
import threading
import time

# Define click function
def click_mouse():
    while not stop_event.is_set():
        pyautogui.click()
        time.sleep(1/240)  # 240 clicks per second

# Define function to stop clicking
def stop_clicking(event):
    global stop_event
    stop_event.set()

# Define function to initiate click
def start_clicking():
    global stop_event
    stop_event = threading.Event()
    click_thread = threading.Thread(target=click_mouse)
    click_thread.start()

# Start main loop
print("Press Enter to start clicking, press P to stop it.")

# Wait for Enter key to initiate clicking
keyboard.wait('enter')
start_clicking()

# Listen for P key to stop clicking
keyboard.on_press_key('p', stop_clicking)

