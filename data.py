import evdev
# import RPi.GPIO
import os
import keyboard

def main():
    #get_number('text.txt')
    unripe, almost_ripe, ripe, too_ripe = data_directory('collect_data')
    append_data(unripe, almost_ripe, ripe, too_ripe)

def get_file_number(file_path):
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            print(int(f.readline()))
    return 0

def update_number():
    pass

def data_directory(file_path):
    directory = os.path.abspath(file_path)
    
    unripe = os.path.join(directory, 'unripe')
    almost_ripe = os.path.join(directory, 'almost_ripe')
    ripe = os.path.join(directory, 'ripe')
    too_ripe = os.path.join(directory, 'too_ripe')

    if not os.path.exists(unripe):
        os.mkdir(unripe)
    if not os.path.exists(almost_ripe):
        os.mkdir(almost_ripe)
    if not os.path.exists(ripe):
        os.mkdir(ripe)
    if not os.path.exists(too_ripe):
        os.mkdir(too_ripe)
    
    return unripe, almost_ripe, ripe, too_ripe

def append_data(unripe, almost_ripe, ripe, too_ripe):
    # need to know what kind of data is gna be append
    unripe_file = 0
    almost_ripe_file = 0
    ripe_file = 0
    too_ripe_file = 0
    while True:
        if keyboard.read_key() == "1":
            os.chdir(unripe)
            with open('test' + str((unripe_file) + 1) + '.txt', 'w') as f:
                unripe_file += 1
                f.write('Hello')
        if keyboard.read_key() == '2':
            os.chdir(almost_ripe)
            with open('test' + str((almost_ripe_file) + 1) + '.txt', 'w') as f:
                almost_ripe_file += 1
                f.write('Hello')
        if keyboard.read_key() == '3':
            os.chdir(ripe)
            with open('test' + str((ripe_file) + 1) + '.txt', 'w') as f:
                ripe_file += 1
                f.write('Hello')
        if keyboard.read_key() == '4':
            os.chdir(too_ripe)
            with open('test' + str((too_ripe_file) + 1) + '.txt', 'w') as f:
                too_ripe_file += 1
                f.write('Hello')
        if keyboard.read_key() == '5':
            break
            

if __name__ == '__main__':
    main()