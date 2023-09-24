import os

def get_only_filename(files):
    lst_file = []
    for file in files:
        lst_file.append(file.split('.')[0])
    return lst_file

def get_highest_numbered_file(path):
    try:
        # List all files in the directory
        files = os.listdir(path)
        print(files)
        new_files = get_only_filename(files)

        # Filter out filenames that aren't numbers and convert them to integers
        numbers = [int(f) for f in new_files if f.isdigit()]
        print(numbers)

        # Return the highest number
        return max(numbers)

    except ValueError:
        # This is raised if there are no numeric files and max() is called on an empty list
        return None

# Replace with the path to your directory
directory_path = 'C:/Users/arunk/OneDrive/Documents/CMKL/the_palm_killer/test'

highest_number = get_highest_numbered_file(directory_path)
if highest_number is not None:
    print(f"The highest numbered file is: {highest_number}")
else:
    print("No numeric file names found in the directory.")
