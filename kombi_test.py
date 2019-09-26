from random import *

liste = []
s = 0           #speicher
k = 0           #Kombinations Länge
n = 0           #Listen Länge


for i in range(10):
    liste.append(i+1)
print(liste)
n = int(len(liste))
k = int(input ("Kombinations Länge: "))


#::::::::::::::MAIN::::::::::::::::::::::::::

print(liste[0:k])
for i in range((n**k)-1):
    for h in  range(n-1):
        s = liste[0]
        liste[0] = liste[h+1]
        liste[h+1] = s
        print(liste[0:k])
    s = liste[0]
    liste[i+1] = liste[0]
    liste[0] = s
    print(liste[0:k])