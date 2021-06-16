import string
import os

from generate_text_image import generate_text_image

from PIL import Image, ImageDraw, ImageFont
from config import (
    FONT,
    FONT_SIZE,
    IMG_HEIGHT,
    COLOUR_SCHEMES,
    BLACK,
    YELLOW
)

if __name__ == "__main__":
    arrows = ["\u2196"]
    input = arrows + list(string.ascii_uppercase) + list(string.digits)

    ocr_dir = 'data/ocr'
    for char in input:
        path = os.path.join('data', 'ocr', f'{char}.png')
        generate_text_image(
            text=char,
            font_path=FONT,
            colour_scheme="branching",
            size=FONT_SIZE,
            path=path
        )

        for i in range(360):
            border_width = 10
            border_colour = YELLOW
            img = Image.open(path)
            img = img.rotate(i)
            draw = Image.new('RGB',
                (img.size[0] + 2 * border_width, img.size[1] + 2 * border_width),
                border_colour)
            mask = Image.new('L', img.size, 255)
            mask = mask.rotate(i)
            draw.paste(img, (border_width, border_width), mask)

            new_path = os.path.join('data', 'ocr', f'{char}_{i}.png')
            draw.save(new_path)