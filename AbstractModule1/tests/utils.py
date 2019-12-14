from random import choice
from string import ascii_letters


def gen_random_text(num_chars):
    return "".join(choice(ascii_letters) for _ in range(num_chars))