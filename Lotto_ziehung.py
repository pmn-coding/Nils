from random import *


lotto = []
s = ""              #speicher
zz = 0

for i in range(49):
    lotto.append(i+1)

print(lotto)

for i in range(1000):
    zz = randint(1,48)
    s = lotto[0]
    lotto[0] = lotto[zz]
    lotto[zz] = s

print(lotto[0:6])