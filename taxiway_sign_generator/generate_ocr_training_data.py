import string
import os
import math

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from config import (
    FONT,
    FONT_SIZE,
    IMG_HEIGHT,
    COLOUR_SCHEMES,
    BLACK,
    YELLOW
)

def generate_char_img(text, font_path, colour_scheme, size, path):
    bg_colour, fg_colour = COLOUR_SCHEMES["branching"]
    img_font = ImageFont.truetype(FONT, FONT_SIZE)

    text_img = Image.new('RGB', (FONT_SIZE, FONT_SIZE))   # for text size and margin determination
    draw = ImageDraw.Draw(text_img)
    text_width, text_height = draw.textsize(text, img_font)

    margin = int((FONT_SIZE - text_height)/2)
    img_width = text_width
    img = Image.new('RGB',(text_width, text_height + 5), bg_colour)

    draw = ImageDraw.Draw(img)
    draw.text((0, 0),
        text, fg_colour, img_font)
    img.save(path)

def get_rotated_corners(size, angle):
    """ TODO: needed? or is using the height and width of rotated and pasted image enough? """
    """ get x_min, x_max, y_min, y_max for rotated rectangle """

    def get_angle(angle):
        """ returns an angle needed for the calculation """
        # coordinates repeat after 180 °
        # coordinates repeat (reversed) after 90 °
        angle = angle % 180
        if angle > 90:
            return angle - 2 * (angle % 90)
        return angle

    gamma = get_angle(angle) * math.pi / 180
    width, height = size
    cx, cy = [int(item / 2) for item in size]
    dist_to_corner = math.sqrt(cx ** 2 + cy ** 2)
    phi = math.atan(cx / cy) + gamma
    x_A = dist_to_corner * math.sin(phi)
    y_A = dist_to_corner * math.cos(phi)
    print(x_A, y_A)
    # symmetry:
    # height = 2 * y_B
    # width = 2 * x_A

if __name__ == "__main__":
    arrows = ["\u2196"]
    #input = arrows + list(string.ascii_uppercase) + list(string.digits)
    input = ["A"]
    dirpath = os.path.join('data', 'ocr')
    global_index = 1

    for char in input:
        Path(os.path.join(dirpath, char)).mkdir(parents=True, exist_ok=True)
        path = os.path.join('data', 'ocr', char, f'{char}.png')
        # generate_text_image(
        #     text=char,
        #     font_path=FONT,
        #     colour_scheme="branching",
        #     size=FONT_SIZE,
        #     path=path
        # )

        """ from generate_text_image start """
        bg_colour, fg_colour = COLOUR_SCHEMES["branching"]
        img_font = ImageFont.truetype(FONT, FONT_SIZE)

        text_img = Image.new('RGB', (FONT_SIZE, FONT_SIZE))   # for text size and margin determination
        draw = ImageDraw.Draw(text_img)
        text_width, text_height = draw.textsize(char, img_font)

        margin = int((FONT_SIZE - text_height)/2)
        img_width = text_width
        img = Image.new('RGB',(text_width, text_height + 5), bg_colour)

        draw = ImageDraw.Draw(img)
        draw.text((0, 0),
            char, fg_colour, img_font)
        img.save(path)
        #img.show()
        """ from generate_text_image end """
        # https://stackoverflow.com/a/51964802

        # for i in range(360):
        #     border_width = 10
        #     border_colour = YELLOW
        #     img = Image.open(path)
        #     img = img.rotate(i)
        #     draw = Image.new('RGB',
        #         (img.size[0] + 2 * border_width, img.size[1] + 2 * border_width),
        #         border_colour)
        #     mask = Image.new('L', img.size, 255)
        #     mask = mask.rotate(i)
        #     draw.paste(img, (border_width, border_width), mask)

        #     new_path = os.path.join('data', 'ocr', f'{global_index}.png')
        #     global_index += 1
        #     draw.save(new_path)
        get_rotated_corners([100, 200], 90)