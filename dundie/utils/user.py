from random import sample
from string import ascii_letters, digits


def generate_simple_password(size=8):
    """Generate a simple randooom password
    [A-Z][a-z][0-9]
    """
    return "".join(sample(ascii_letters + digits, size))
