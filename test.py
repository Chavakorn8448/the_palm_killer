from PIL import Image

# Image size
width, height = 300, 300

# Color: in this case, it's red. You can choose any RGB value.
color = (255, 0, 0)

# Create an image with the given color
image = Image.new('RGB', (width, height), color)

# Save the image as a .jpg file
image.save('0.jpg')