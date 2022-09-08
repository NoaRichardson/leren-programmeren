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

print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 43.12 euro')