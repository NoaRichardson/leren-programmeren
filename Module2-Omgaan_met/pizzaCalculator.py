#pizzaCalculator.py
#Noa Richardson opdracht: Pizza calculator

print('Hoeveel pizza wilt u?')

pizzal = int (input('Large 9.99 ='))
pizzam = int (input('Medium 7.99 ='))
pizzas = int (input('Small 5.99 ='))

prijsl = pizzal * 9.99
prijsm = pizzam * 7.99
prijss = pizzas * 5.99

totaal = prijsl + prijsm + prijss

print('---------------------------------------------')
print(f'Pizza Large = {pizzal}  | {prijsl}')
print(f'Pizza Medium = {pizzam} | {prijsm}')
print(f'Pizza Small = {pizzas}  | {prijss}')
print(f'Totale Prijs = {totaal} euro')
print('---------------------------------------------')