#Feestlunch.py


print("Hoeveel je moet betalen...")
croissantjes = input('Hoeveel croissantjes wilt u?')
croissantjes = int(croissantjes)

stokbroden = input('Hoeveel stokbroden wilt u?')
stokbroden = int(stokbroden)

prijsC = 39
prijsS = 278

PrijsC = croissantjes * prijsC
PrijsS = stokbroden * prijsS

Prijs = PrijsC + PrijsS
print('Prijs', Prijs ,'cent')

kortingsbonnen = input('Hoeveel kortingsbonnen heeft u?')
kortingsbonnen = int(kortingsbonnen)
kb = 50
korting = kortingsbonnen * kb
Totaal = Prijs - korting

print('Totaal', Totaal ,'cent')

print(f'De feestlunch kost je bij de bakker {Totaal} cent voor de {croissantjes} croissantjes en de {stokbroden} stokbroden als de {kortingsbonnen} kortingsbonnen nog geldig zijn!')

