""" generate text image """

from PIL import Image, ImageDraw, ImageFont
from config import FONT, FONT_SIZE, IMG_HEIGHT, COLOUR_SCHEMES

def generate_text_image(text, font_path, colour_scheme, size, path):
    """! generates an image of a text

    @param text string to draw
    @param font_path path to chosen font
    @param colour_scheme the type of sign to create ("position", "branching", or "warning")
    @param size the height for the image
    @param path path to save the image under

    """
    bg_colour, fg_colour = COLOUR_SCHEMES[colour_scheme]
    img_font = ImageFont.truetype(font_path, FONT_SIZE)

    text_img = Image.new('RGB', (size, size))   # for text size and margin determination
    draw = ImageDraw.Draw(text_img)
    text_width, text_height = draw.textsize(text, img_font)

    margin = int((size - text_height)/2)
    img_width = 2 * margin + text_width

    img = Image.new('RGB',(img_width, size), bg_colour)
    draw = ImageDraw.Draw(img)
    draw.text((margin, margin),
           text, fg_colour, img_font)
    img.save(path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str)
    parser.add_argument('colour_scheme', type=str)
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    generate_text_image(
        args.text,
        FONT,
        args.colour_scheme,
        IMG_HEIGHT,
        args.path
    )
