from fruitmand import fruitmand

round = 0
niet_round = 0
kleur = []
for fruit in fruitmand:
    kleur.append(fruit['color'])
fruit_kleur = ""

while fruit_kleur not in kleur:
    fruit_kleur = input("Kies een kleur")
    if fruit_kleur not in kleur:
        print(f"De kleur {fruit_kleur} zit niet in fruitmand")

fruit_round = []
for fruit in fruitmand:
    if fruit['color'] in {fruit_kleur}:
        fruit_round.append(fruit['round'])
    
for tf in fruit_round:
    if tf is True:
        round = round + 1
    elif tf is False:
        niet_round = niet_round + 1
    
if round > niet_round:
    cr = round - niet_round
    print(f'Er zijn {cr} meer ronde vruchten dan niet ronde vruchten in de kleur {fruit_kleur}')

elif round < niet_round:
    cr = niet_round - round 
    print(f'Er zijn {cr} minder ronde vruchten dan niet ronde vruchten in de kleur {fruit_kleur}')

elif round == niet_round:
    print(f'Er zijn eveveel ronde en niet ronde vruchten in de kleur {fruit_kleur}')

        
