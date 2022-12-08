from fruitmand import fruitmand

dictfruit = {
    'name' : 'watermeloen',
    'weight': 1700,
    'color' : 'green',
    'round' : True
}
fruitmand.append(dictfruit)

for fruit in fruitmand:
    print(fruit['weight'])