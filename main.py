from random import *


def generate_ip():
    return (f"{randrange(256)}.{randrange(256)}.{randrange(256)}.{randrange(256)}")


print(generate_ip())
