""" add a border frame to the image """

from PIL import Image
from config import BLACK, YELLOW

def add_border(image_path, border_colour, border_width):
    """!

    @param image_path path to the image
    @param border_colour RGB tuple
    @param border_width frame size in px

    """
    img = Image.open(image_path)

    draw = Image.new('RGB',
        (img.size[0] + 2 * border_width, img.size[1] + 2 * border_width),
        border_colour)
    draw.paste(img, (border_width, border_width))

    draw.save(image_path)

def determine_border_colour(directions):
    """! determines border colour by represented directions

    @param directions dict with directions

    """
    return YELLOW if [*(directions)] == ["current"] else BLACK
