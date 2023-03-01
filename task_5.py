import random
import string


def get_random_password(length=8) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.sample(alphabet, length))


print(get_random_password())
