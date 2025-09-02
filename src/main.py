
import random
import string
# from random import uniform
# from time import sleep
# import sys

def process_string(length):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choices(letters, k=length))

# for x in process_string:
#    print(process_string(50), end='')
#    sys.stdout.flush()
#     sleep(uniform(0, 0.3))

# TODO: MAKE THE TYPEWRITER EFFECT WORK