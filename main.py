from random import choice, randrange
from string import ascii_uppercase as letter


def generate_index():
    return (
        f"{choice(letter)}{choice(letter)}{randrange(100)}_{randrange(100)}{choice(letter)}{choice(letter)}")


print(generate_index())
