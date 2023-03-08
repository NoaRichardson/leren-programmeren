getal = int(input("Kies een getal"))
cijfer = getal + 1
ruit = ""

for x in range(1, cijfer):
    y = str(x)
    ruit += y
    print(ruit + "")

for a in range(cijfer, 1, -1):
    b = str(a)
    ruit.replace(b, "")
    print(ruit + "")
