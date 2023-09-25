import evdev
from evdev import ecodes
import os
from PIL import Image
from picamera2 import Picamera2, Preview

def take_pic(filename):
    picam2 = Picamera2()
    picam2.start_preview(Preview.NULL)
    picam2.start()
    time.sleep(2)
    metadata = picam2.capture_file("/home/traffy/the_palm_killer/" + filename + ".jpg")
    picam2.close()
    print("captured")

# get last file number
def get_only_filename(files):
    lst_file = []
    for file in files:
        lst_file.append(file.split('.')[0])
    return lst_file

def get_highest_numbered_file(path):
    try:
        # List all files in the directory
        files = os.listdir(path)
        new_files = get_only_filename(files)

        # Filter out filenames that aren't numbers and convert them to integers
        numbers = [int(f) for f in new_files if f.isdigit()]

        # Return the highest number
        return max(numbers)

    except ValueError:
        # This is raised if there are no numeric files and max() is called on an empty list
        return None
    
def crop_image(image):
    if image.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Calculate the middle region to crop
        width, height = image.size
        new_width, new_height = width // 2, height // 2
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2

        # Crop the middle of the image
        cropped_image = image.crop((left, top, right, bottom))

        # Save the cropped image to the destination folder
        return cropped_image

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

directory = os.path.abspath("/home/traffy/the_palm_killer")

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

unripe_last_num = get_highest_numbered_file(unripe)
almost_ripe_last_num = get_highest_numbered_file(almost_ripe)
ripe_last_num = get_highest_numbered_file(ripe)
too_ripe_last_num = get_highest_numbered_file(too_ripe)

if unripe_last_num is None:
    unripe_last_num = 1
if almost_ripe_last_num is None:
    almost_ripe_last_num = 1
if ripe_last_num is None:
    ripe_last_num = 1
if too_ripe_last_num is None:
    too_ripe_last_num = 1

# Infinite loop to check for key events
for event in keyboard.read_loop():
# Check if a key is pressed down and if it's the '1' key
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_1:
        print("'1' key pressed!")
        os.chdir(unripe)
        take_pic(unripe_last_num)
        unripe_last_num += 1
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_2:
        print("'2' key pressed!")
        os.chdir(almost_ripe)
        take_pic(almost_ripe_last_num)
        almost_ripe_last_num += 1
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_3:
        print("'3' key pressed!")
        os.chdir(ripe)
        take_pic(ripe_last_num)
        ripe_last_num += 1
    if event.type == ecodes.EV_KEY and event.value == 1 and event.code == ecodes.KEY_4:
        print("'4' key pressed!")
        os.chdir(too_ripe)
        take_pic(too_ripe_last_num)
        too_ripe_last_num += 1