Achse = ""
for i in range(125):        #Zahl ändern um x-Achsenlänge zu ändern
    Achse += "-"
ac = 0.01                  #auflösung
for x in range(-10,10,1):
    c = 0
    if x == 0:
        print(Achse)
    else:
        y = 1/x**2
        #print("Vor",y)
        if not y % ac == 0:
            y -= y % ac
            #print("Nach",y)
        while not y <= 0:
            y -= ac
            c += 1
        #print("Nachc",c)
        zeile = c*' ' + "x"
        print("|", zeile)
