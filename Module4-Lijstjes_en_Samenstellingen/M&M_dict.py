import random

mnm = ("rood", "blauw", "groen", "geel", "bruin")
aantal_mnm = int(input("Hoeveel M&M wil je?"))
dictmnm = {}

for x in range(aantal_mnm):
    kleur = random.choice(mnm)
    if kleur in dictmnm:
        dictmnm[kleur] += 1
    else:
        dictmnm[kleur] = 1
    
print(dictmnm)