import random
oranje = 0
blauw = 0
groen = 0
bruin = 0

zak_mnm = []
aantal_mnm = int(input("Hoeveel M&M?"))
for x in range(aantal_mnm):
    getal = random.randint(1, 4)
    if getal == 1:
        zak_mnm.append("oranje")
    elif getal == 2:
        zak_mnm.append("blauw")
    elif getal == 3:
        zak_mnm.append("groen")
    elif getal == 4:
        zak_mnm.append("bruin")

print(zak_mnm)


