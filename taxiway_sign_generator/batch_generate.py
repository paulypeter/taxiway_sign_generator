""" batch generation of taxiway signs """

from sign_generator import generate_image

args = {
    "up_left": None,
    "left": None,
    "down_left": None,
    "current": None,
    "up_right": None,
    "right": None,
    "down_right": None
}

for i in range(99):
    args = {"current": "A" + str(i + 1)}
    generate_image(args)

