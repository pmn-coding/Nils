#with 0
def zero(b, l):
    for i in range(l):
        print(b*"0")

#with stars
def sq(b, l):
    for i in range(l):
        print(b*"*")

#only border
#Problem sind die Zeichenabstände. * ist nicht so groß wie ein Leerzeichen
def bs(b, l):
    print(b*"* ")
    for i in range(l-2):
        print("* ",(b-1)*" ", "*")
    print(b*"* ")



breite = int(input("Breite: "))
laenge = int(input("Länge: "))

sq(breite, laenge)
print()
zero(breite, laenge)
print()
bs(breite, laenge)
print()