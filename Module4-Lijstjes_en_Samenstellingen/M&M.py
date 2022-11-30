import random
oranje = 0
blauw = 0
groen = 0
bruin = 0

mnm = [oranje, blauw, groen, bruin]
aantal_mnm = int(input("Hoeveel M&M?"))
for x in range(aantal_mnm):
    getal = random.randint(1, 4)
    if getal == 1:
        oranje = oranje + 1
    elif getal == 2:
        blauw = blauw + 1
    elif getal == 3:
        groen = groen + 1
    elif getal == 4:
        bruin = bruin + 1

print("Aantal M&M")
print(f"Orange: {oranje}")
print(f"Blauw: {blauw}")
print(f"Groen: {groen}")
print(f"Bruin: {bruin}")
