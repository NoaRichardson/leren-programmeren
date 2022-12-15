from fruitmand import fruitmand

langste_fruit = []
aantal_letters = []

kleur = ['geel', 'groen', 'oranje', 'geel', 'rood', 'bruin', 'geel']
i = 0

for fruit in fruitmand:
    fruit['color'] = kleur[i]
    i = i + 1

for fruit in fruitmand:
    letters =(len(fruit['name']))
    aantal_letters.append(letters)

langste = max(aantal_letters)

while langste is not (len(fruit['name'])):
    for fruit in fruitmand:
        (len(fruit['name']))
        if langste == (len(fruit['name'])):
            langste_fruit.append(fruit['name'])
            langste_fruit.append(fruit['color'])
            langste_fruit.append(fruit['weight'])
            break


print(f'De {langste_fruit[0]}({langste} letters) heeft een {langste_fruit[1]} kleur en het gewicht van {langste_fruit[2] / 1000} kg')
            