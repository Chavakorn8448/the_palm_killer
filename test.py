from PIL import Image

def change_color(image):
    image = Image.open(image)
    r, g, b = image.split()

    r = r.point(lambda p: p * 0.8)
    g = g.point(lambda p: p * 1.5)
    b = b.point(lambda p: p * 1.5)
    new_image = Image.merge('RGB', (r, g, b))
    return new_image

x = change_color('red_image.jpg')
x.save('new_image.jpg')