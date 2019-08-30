from time import *
from sys import *
from random import *


text = "Hello, My name is Nils"


for char in text:
    delay = "0.0" + str(randrange(1, 4, 1))
    stdout.write(char)
    stdout.flush()
    sleep(float(delay))