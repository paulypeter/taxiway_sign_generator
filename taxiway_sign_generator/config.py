""" config file for taxiway_sign_generator """

DATA_DIR = 'data'

DIRECTION_ARROWS = {
    "up_left": "\u2196",
    "left": "\u2190",
    "down_left": "\u2199",
    "current": "",
    "up_right": "\u2197",
    "right": "\u2192",
    "down_right": "\u2198"
}

IMG_HEIGHT = 112
FONT_SIZE = int(IMG_HEIGHT/100) * 100

YELLOW = (240, 231, 15)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

COLOUR_SCHEMES = {   # (bg, fg)
    "branching": (YELLOW, BLACK),
    "position": (BLACK, YELLOW),
    "warning": (RED, WHITE)
}

#FONT = "/home/peter/Roadgeek2014SeriesD2.ttf"
#font = "RG2014D.ttf"
FONT = "/usr/share/fonts/OTF/overpass-semibold.otf"
