def quadratzahl(b, e):
    i = 0
    while i*i < b:
        i = i + 1
    while i*i <= e:
        print(i*i)
        i += 1

start = int(input("Anfang: "))
end = int(input("Ende: "))

quadratzahl(start, end)
