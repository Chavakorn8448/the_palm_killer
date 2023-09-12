import evdev
from evdev import ecodes

# Search for the device. In this example, we're looking for keyboards.
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
keyboard_devices = [device for device in devices if 'keyboard' in device.name.lower()]

# If no keyboards are found, exit.
if not keyboard_devices:
    print("No keyboards found!")
    exit()

# Print all detected keyboard devices
print("Detected keyboard devices:")
for idx, kbd in enumerate(keyboard_devices, 1):
    print(f"{idx}. {kbd.name}")

# Use the first keyboard found. You might need to adjust this if you have multiple keyboard devices.
keyboard = keyboard_devices[2]

print(f"\nListening for key press on device: {keyboard.name}")

# Infinite loop to check for key events
for event in keyboard.read_loop():
    # Check if a key is pressed down and if it's the '1' key
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_1:
        print("'1' key pressed!")
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_2:
        print("'2' key pressed!")
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_3:
        print("'3' key pressed!")
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_4:
        print("'4' key pressed!")