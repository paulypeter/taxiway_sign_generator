import os

from generate_text_image import generate_text_image
from sign_generator import combine_images
from add_border import add_border
from config import *

text2 = "26-08" #DIRECTION_ARROWS["left"] + "A" + DIRECTION_ARROWS["right"]
# text = "☣"
text1 = "C"
path1 = os.path.join(DATA_DIR, "custom", f'{text1}.png')
path2 = os.path.join(DATA_DIR, "custom", f'{text2}.png')
generate_text_image(text2, FONT, "warning", IMG_HEIGHT, path2)
generate_text_image(text1, FONT, "position", IMG_HEIGHT, path1)
generate_text_image(text, "/usr/share/fonts/TTF/DejaVuSans.ttf", "branching", IMG_HEIGHT, "bio.png")

combined_path = os.path.join(DATA_DIR, "custom", f'{text1}_{text2}.png')
combine_images([path1, path2], combined_path)

add_border(combined_path, BLACK, 15)
