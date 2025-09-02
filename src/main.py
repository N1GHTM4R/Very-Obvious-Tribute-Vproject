
import random
import string
from random import uniform
from time import sleep
import sys

def process_string(length):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choices(letters, k=length))

while True:
    generated_string = process_string(random.randint(1, 50))
    for char in generated_string:
        print(char, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.1))
    print()
    
