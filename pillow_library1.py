import os
from PIL import Image,ImageDraw,ImageFont


def get_hex_to_rgba(str):
    new_str = str.lstrip("#")
    return tuple(int(new_str[i:i+2],16) for i in (0,2,4))

def get_position(img,logo):
    return {
        "topleft":(45,0),
        "topmiddle":((img.width // 2) - (logo.width // 2),0),
        "topright":((img.width - logo.width) - 45,0),
        "centerleft":(0,(img.height // 2) - (logo.height // 2)),
        "centermiddle":((img.width // 2) - (logo.width // 2),(img.height // 2) - (logo.height // 2)),
        "centerright":((img.width - logo.width) - 45,(img.height // 2) - (logo.height // 2)),
        "bottomleft":(45,(img.height - logo.height) + 45),
        "bottommiddle":((img.width // 2) - (logo.width // 2),(img.height - logo.height) + 45),
        "bottomright":((img.width - logo.width) - 45,(img.height - logo.height) + 45),
    }

img = Image.new("RGB",(998,998),color=get_hex_to_rgba("#eb4034"))

title_font = ImageFont.truetype("./poppins/Poppins-BoldItalic.ttf",35)

logo = Image.open("./logo4.png")

logo.thumbnail(((img.width * 35) / 100,(img.height * 25) / 100),Image.ANTIALIAS)

print((logo.width,logo.height))

img.paste(logo,get_position(img,logo)["bottomright"],logo)

title_text = "This is Made with Pillow"

draw = ImageDraw.Draw(img)

w,h = draw.textsize(title_text)

draw.text(((img.width / 2) - 200,(img.height / 2)),title_text,font=title_font,fill=(255,255,255,128))

img.save("save.png")

img.show()