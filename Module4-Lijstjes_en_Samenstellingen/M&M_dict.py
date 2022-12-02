import random

mnm = ["rood", "blauw", "groen", "geel", "bruin"]
aantal_mnm = int(input("Hoeveel M&M wil je?"))
dictmnm = {}

for mm in mnm:
    dictmnm[mm] = 0

for x in range(aantal_mnm):
    rnd = random.randint(0, 4)
    dictmnm[mnm[rnd]] += 1

for mm in mnm:
    if dictmnm[mm] == 0:
        dictmnm.pop(mm)
    
print(dictmnm)