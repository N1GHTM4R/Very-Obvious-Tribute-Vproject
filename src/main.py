
import random
import string


def process_string(length):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choices(letters, k=length))


print(process_string(50))
