import random
import string


def generate_numeric_password(length: int = 8) -> str:
    """
    Generates a random numeric password of the given length.
    """
    return ''.join(random.choice(string.digits) for i in range(length))
