#speelhal.py

print('Toegangtickets')

personen = int (input('Met hoeveel'))
PrijsToegangtickets = personen * 7.45
print('Prijs', PrijsToegangtickets ,'euro')

print('VIP-VR Gameseat')

tijd = int (input('Hoeveel minuten?'))
prijsVR = tijd / 5 * 0.37
PrijsVR = prijsVR * personen
print('PrijsVR', PrijsVR ,'euro')

Totaal = PrijsToegangtickets + PrijsVR
print('Totaal', Totaal ,'euro')