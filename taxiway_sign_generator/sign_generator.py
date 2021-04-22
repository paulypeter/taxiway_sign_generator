""" generate taxiway signs """

import os
from pathlib import Path
from PIL import Image

from generate_direction_images import generate_direction_images
from config import DATA_DIR, IMG_HEIGHT
from add_border import add_border, determine_border_colour

def combine_images(image_list, combined_img_path):
    """! combines multiple images horizontally

    @param image_list list of paths to image files
    @param combined_img_name name for the created image file

    """
    images, image_width = [], []
    for img in image_list:
        current_image = Image.open(img)
        images.append(current_image)
        image_width.append(current_image.size[0])
    combined = Image.new('RGB', (sum(image_width), IMG_HEIGHT))
    x_position = 0
    for (image, size) in zip(images, image_width):
        combined.paste(image, (x_position, 0))
        x_position += size
    combined.save(combined_img_path)

def init_data_dir(directions):
    """! initialise directories

    @param directions dict of branching directions

    """
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    for direction in directions:
        path = os.path.join(DATA_DIR, direction)
        Path(path).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(DATA_DIR, "signs")).mkdir(parents=True, exist_ok=True)

def generate_image(directions):
    """!

    @param directions dict for user input

    """
    init_data_dir(directions)

    image_path_list, combined_name = generate_direction_images(directions)
    combined_img_path = os.path.join(DATA_DIR, "signs", f'{combined_name}.png')
    combine_images(image_path_list, combined_img_path)

    border_colour = determine_border_colour(directions)
    add_border(os.path.join(DATA_DIR, "signs", f'{combined_name}.png'), border_colour, 10)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--up-left', '-ul', dest='up_left', type=str)
    parser.add_argument('--left', '-l', dest='left', type=str)
    parser.add_argument('--down-left', '-dl', dest='down_left', type=str)
    parser.add_argument('--current', '-c', dest="current", type=str)
    parser.add_argument('--up-right', '-ur', dest='up_right', type=str)
    parser.add_argument('--right', '-r', dest='right', type=str)
    parser.add_argument('--down-right', '-dr', dest='down_right', type=str)

    args = parser.parse_args()

    user_input = {}
    for arg in vars(args):
        attr = getattr(args, arg)
        if attr is not None:
            user_input[arg] = getattr(args, arg)

    generate_image(user_input)
