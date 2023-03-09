getal = int(input("Kies een getal"))
cijfer = getal + 1
ruit = []

for x in range(1, cijfer):
    y = str(x)
    ruit += y
    print(ruit)

for a in range(getal, 0, -1):
    b = str(a)
    ruit.remove(b)
    print(ruit)
