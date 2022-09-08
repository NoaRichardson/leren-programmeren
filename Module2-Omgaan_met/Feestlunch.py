#Feestlunch.py


print("Hoeveel je moet betalen...")
croissantjes = input('Hoeveel croissantjes wilt u?')
croissantjes = int(croissantjes)

stokbroden = input('Hoeveel stokbroden wilt u?')
stokbroden = int(stokbroden)

prijsC = 0.39
prijsS = 2.78

PrijsC = croissantjes * prijsC
PrijsS = stokbroden * prijsS

Prijs = PrijsC + PrijsS
print('Prijs', Prijs ,'euro')

kortingsbonnen = input('Hoeveel kortingsbonnen heeft u?')
kortingsbonnen = int(kortingsbonnen)
kb = 0.50
korting = kortingsbonnen * kb
Totaal = Prijs - korting

print('Totaal', Totaal ,'euro')

print('De feestlunch kost je bij de bakker 10.69 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')

