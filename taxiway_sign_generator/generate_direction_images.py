""" generate separate images for branching taxiways etc. """

import os
from pathlib import Path
from PIL import Image

from generate_text_image import generate_text_image
from config import DATA_DIR, IMG_HEIGHT, FONT, DIRECTION_ARROWS

def generate_direction_images(directions):
    """! generates images for branching or current taxiway

    @param directions dict of directions and according taxiway

    """
    image_list = []
    combined_name = ""
    for direction in directions:
        twy = directions[direction]
        if twy is not None:
            colour_scheme = "position" if direction == "current" else "branching"
            text = (DIRECTION_ARROWS[direction] + twy
                if direction.endswith("left") else
                twy + DIRECTION_ARROWS[direction])
            path = os.path.join(DATA_DIR, direction, f'{twy}_{IMG_HEIGHT}.png')
            img_file = Path(path)
            if not img_file.is_file():
                generate_text_image(
                    text,
                    FONT,
                    colour_scheme,
                    IMG_HEIGHT,
                    path
                )
            combined_name += text
            if image_list:
                if (image_list[-1].find("left") > 0 and direction.endswith("left") or
                image_list[-1].find("right") > 0 and direction.endswith("right")):
                    divider_path = os.path.join(DATA_DIR, f'divider_{IMG_HEIGHT}.png')
                    image_list.append(divider_path)
                    divider_file = Path(divider_path)
                    if not divider_file.is_file():
                        create_divider(IMG_HEIGHT)
            image_list.append(path)
    return (image_list, combined_name)

def create_divider(size):
    """! creates a divider image

    @param size divider height

    """
    divider = Image.new('RGB', (int(size / 15), size))
    divider.save(os.path.join(DATA_DIR, f'divider_{size}.png'))
