from fruitmand import fruitmand

# print(fruitmand[1].get("weight"))
for fruit in fruitmand:
    if fruit['name'] == 'appel':
        print(fruit['weight'])
        break