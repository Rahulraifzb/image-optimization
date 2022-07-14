
from PIL import Image
import math


def resize_canvas(old_image_path="img1.jpg", new_image_path="save.jpg",
                  canvas_width=500, canvas_height=500):
    """
    Place one image on another image.

    Resize the canvas of old_image_path and store the new image in
    new_image_path. Center the image on the new canvas.
    """
    img = Image.open(old_image_path)
    old_width, old_height = img.size

    # Center the image
    x1 = int(math.floor((canvas_width - old_width) / 2))
    y1 = int(math.floor((canvas_height - old_height) / 2))

    mode = img.mode
    if len(mode) == 1:  # L, 1
        new_background = (255)
    if len(mode) == 3:  # RGB
        new_background = (255, 255, 255)
    if len(mode) == 4:  # RGBA, CMYK
        new_background = (255, 255, 255, 255)

    img.resize((canvas_width, canvas_height),Image.ANTIALIAS)
    img.save(new_image_path)

    img.show()

    print(img.width,img.height)
resize_canvas()
