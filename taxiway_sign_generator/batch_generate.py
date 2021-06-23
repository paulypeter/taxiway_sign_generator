""" batch generation of taxiway signs """
import string
import random

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

directions_list = ("up_left", "left", "down_left", "current", "up_right", "right", "down_right")
letters_list = list(string.ascii_uppercase)

for i in range(100):
    number_of_fields = random.randint(1, 4)
    directions = random.sample(directions_list, number_of_fields)
    letters = random.sample(letters_list, number_of_fields)
    for i in range(number_of_fields - 1):
        add_number = random.randint(1, 50)
        args[directions[i]] = letters[i]
        if add_number == 1:
            args[directions[i]] += str(random.randint(1,15))
    args["current"] = letters[-1]
    generate_image(args)

    for i in range(number_of_fields - 1):
        args[directions[i]] = None
    args["current"] = None
