import random

mnm_kleuren = ['orange', 'blauw', 'groen', 'bruin']

zak_mnm = []
aantal_mnm = int(input("Hoeveel M&M?"))
for x in range(aantal_mnm):
    kleur = random.choice(mnm_kleuren)
    zak_mnm.append(kleur)


print(zak_mnm)


