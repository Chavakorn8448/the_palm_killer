import evdev
from evdev import ecodes

# Search for the device. In this example, we're looking for keyboards.
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
keyboard_devices = [device for device in devices if 'keyboard' in device.name.lower()]

# If no keyboards are found, exit.
if not keyboard_devices:
    print("No keyboards found!")
    exit()

# Use the first keyboard found. You might need to adjust this if you have multiple keyboard devices.
keyboard = keyboard_devices[0]

print(f"Listening for 'a' key press on device: {keyboard.name}")

# Infinite loop to check for key events
for event in keyboard.read_loop():
    # Check if a key is pressed down and if it's the 'a' key
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_A:
        print("'a' key pressed!")
        # Do your logic here, like appending data to a directory
