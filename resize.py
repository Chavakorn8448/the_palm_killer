import os
from tkinter import Tk, filedialog, Button, Label
from PIL import Image

def resize_image(img_path, save_path):
    target_pixels = 8e6  # 8MP
    with Image.open(img_path) as img:
        width, height = img.size
        aspect_ratio = width / height
        new_width = int((target_pixels * aspect_ratio) ** 0.5)
        new_height = int(new_width / aspect_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        print(f"Saving to: {save_path}")  # Debugging line
        img.save(save_path)

def select_folder_and_resize():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    if not folder_path:
        return

    # Create a new directory for the resized images
    output_folder = os.path.join(os.path.dirname(folder_path), "Resized_8MP")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(output_folder, filename)
            
            print(f"Processing: {filename}")  # Debugging line

            try:
                resize_image(input_file_path, output_file_path)
                status_label.config(text=f"Resized: {filename}")
            except Exception as e:
                print(f"Exception: {str(e)}")  # Debugging line
                status_label.config(text=f"Error with {filename}: {str(e)}")
                continue

    status_label.config(text="All images resized successfully!")

root = Tk()
root.title("Resize Images to 8MP")

instructions = Label(root, text="Select a folder to resize all its images to 8MP")
instructions.pack(pady=20)

browse_btn = Button(root, text="Browse Folder", command=select_folder_and_resize)
browse_btn.pack(pady=20)

status_label = Label(root, text="")
status_label.pack(pady=20)

root.mainloop()
