from fruitmand import fruitmand

fruitmand.sort(reverse = True, key=lambda fruit:fruit['weight'])
for fruit in fruitmand:
    print(fruit['name'], fruit['weight'])
