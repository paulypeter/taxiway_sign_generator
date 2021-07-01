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

# TODO: enable multiple fonts

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

def get_rotated_size(size, angle):
    """ TODO: needed? or is using the height and width of rotated and pasted image enough? """
    """ get x_min, x_max, y_min, y_max for rotated rectangle """

    def get_angle(angle):
        """ returns an angle needed for the calculation """
        # coordinates repeat after 180 °
        # coordinates repeat (reversed) after 90 °
        # TODO: repeat doesn't work!
        angle = angle % 180
        if angle > 90:
            return angle - 2 * (angle % 90)
        return angle

    gamma = get_angle(angle) * math.pi / 180
    width, height = size
    cx, cy = [int(item / 2) for item in size]
    dist_to_corner = math.sqrt(cx ** 2 + cy ** 2)
    phi = math.atan(cx / cy) + gamma
    phi_2 = gamma - math.atan(cx / cy)
    x_A = dist_to_corner * math.sin(phi)
    y_A = dist_to_corner * math.cos(phi)
    x_B = dist_to_corner * math.sin(phi_2)
    y_B = dist_to_corner * math.cos(phi_2)
    # (x_min, y_1), (x_2, y_min), (x_max, y_3), (x_4, y_max)
    x_min = 0
    x_max = 2 * x_A
    x_2 = x_A - x_B
    y_min = 0
    y_max = 2 * y_B
    y_1 = y_B - y_A
    x_4 = x_max - x_2
    y_3 = y_max - y_1
    if angle % 180 < 90:
        res = ((x_min, y_1), (x_2, y_min), (x_max, y_3), (x_4, y_max))
    elif angle % 180 < 180:
        res = ((x_min, y_3), (x_2, y_max), (x_max, y_1), (x_4, y_min))
    return res

if __name__ == "__main__":
    arrows = ["\u2191"]
    #input = arrows + list(string.ascii_uppercase) + list(string.digits)
    
    dirpath = os.path.join('data', 'ocr')
    global_index = 1

    for char in arrows:
        Path(os.path.join(dirpath, char)).mkdir(parents=True, exist_ok=True)
        path = os.path.join('data', 'ocr', f'{char}.png')
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
        img = Image.new('RGB',(text_width + 5, text_height + 5), bg_colour)

        draw = ImageDraw.Draw(img)
        draw.text((0, 0),
            char, fg_colour, img_font)
        img.save(path)
        #img.show()
        """ from generate_text_image end """
        # https://stackoverflow.com/a/51964802

        for i in range(360):
            border_width = 10
            border_colour = YELLOW
            img = Image.open(path)
            A, B, C, D = get_rotated_size(img.size, i)
            x_max = max([x[0] for x in [A, B, C, D]])
            y_max = max([x[1] for x in [A, B, C, D]])
            max_dim = max(img.size)
            draw = Image.new('RGB',
                (int(x_max + 2 * border_width), int(y_max + 2 * border_width)),
                border_colour)
            mask = Image.new('L', img.size, 255)
            img = img.rotate(i, expand=True)
            mask = mask.rotate(i, expand=True)
            draw.paste(img, (border_width, border_width), mask)
            # draw_line = ImageDraw.Draw(draw)
            # draw_line.line((A[0] + border_width, A[1] + border_width, B[0] + border_width, B[1] + border_width), fill=0)
            # draw_line.line((B[0] + border_width, B[1] + border_width, C[0] + border_width, C[1] + border_width), fill=0)
            # draw_line.line((C[0] + border_width, C[1] + border_width, D[0] + border_width, D[1] + border_width), fill=0)
            # draw_line.line((D[0] + border_width, D[1] + border_width, A[0] + border_width, A[1] + border_width), fill=0)
            new_path = os.path.join('data', 'ocr', f'{str(global_index).zfill(3)}.png')
            ground_truth_path = os.path.join('data', 'ocr', f'{str(global_index).zfill(3)}.txt')
            global_index += 1
            pos_str = ",".join(
                [
                    "4",
                    str((border_width + A[0]) / draw.size[0]),
                    str((border_width + B[0]) / draw.size[0]),
                    str((border_width + C[0]) / draw.size[0]),
                    str((border_width + D[0]) / draw.size[0]),
                    str((border_width + A[1]) / draw.size[1]),
                    str((border_width + B[1]) / draw.size[1]),
                    str((border_width + C[1]) / draw.size[1]),
                    str((border_width + D[1]) / draw.size[1]),
                    "",
                    ""
                ]
            )
            with open(ground_truth_path, "w") as ground_truth_file:
                ground_truth_file.write(
                    pos_str
                )
            draw.save(new_path)