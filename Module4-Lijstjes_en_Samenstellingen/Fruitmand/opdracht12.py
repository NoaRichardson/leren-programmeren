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
            naam =(fruit['name'])
            kleur_fruit = (fruit['color'])
            gewicht =(fruit['weight'])
            break


print(f'De {naam} ({langste} letters) heeft een {kleur_fruit} kleur en het gewicht van {gewicht / 1000} kg')
            