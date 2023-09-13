import evdev
from evdev import ecodes
import os

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

directory = os.path.abspath('test.py')

unripe = os.path.join(directory, 'unripe')
almost_ripe = os.path.join(directory, 'almost_ripe')
ripe = os.path.join(directory, 'ripe')
too_ripe = os.path.join(directory, 'too_ripe')

if not os.path.exists(unripe):
     os.mkdir(unripe)
     unripe_file = os.path.join(unripe, 'unripe.txt')
     if not os.path.exists(unripe_file):
          os.chdir(unripe)
          with open('unripe.txt', 'w') as f:
               pass
if not os.path.exists(almost_ripe):
     os.mkdir(almost_ripe)
     almost_ripe_file = os.path.join(almost_ripe, 'almost_ripe.txt')
     if not os.path.exists(almost_ripe_file):
          os.chdir(almost_ripe)
          with open('almost_ripe.txt', 'w') as f:
               pass
if not os.path.exists(ripe):
     os.mkdir(ripe)
     ripe_file = os.path.join(ripe, 'ripe.txt')
     if not os.path.exists(ripe_file):
          os.chdir(ripe)
          with open('ripe.txt', 'w') as f:
               pass
if not os.path.exists(too_ripe):
     os.mkdir(too_ripe)
     too_ripe_file = os.path.join(too_ripe, 'too_ripe.txt')
     if not os.path.exists(too_ripe_file):
          os.chdir(too_ripe)
          with open('too_ripe.txt', 'w') as f:
               pass

# Infinite loop to check for key events
for event in keyboard.read_loop():
# Check if a key is pressed down and if it's the '1' key
     if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_1:
          print("'1' key pressed!")
          os.chdir(unripe)
          with open('unripe.txt', 'a') as f:
               f.write('1') # write the data recieve
     if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_2:
          print("'2' key pressed!")
          os.chdir(almost_ripe)
          with open('almost_ripe.txt', 'a') as f:
               f.write('2') # write the data recieve
     if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_3:
          print("'3' key pressed!")
          os.chdir(ripe)
          with open('ripe.txt', 'a') as f:
               f.write('3') # write the data recieve
     if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_4:
          print("'4' key pressed!")
          os.chdir(too_ripe)
          with open('too_ripe.txt', 'a'):
               f.write('4') # write the data recieve