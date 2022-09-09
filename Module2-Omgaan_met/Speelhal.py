#speelhal.py

print('Toegangtickets')

personen = int (input('Met hoeveel'))
PrijsToegangtickets = personen * 745
print('Prijs', PrijsToegangtickets ,'cent')

print('VIP-VR Gameseat')

tijd = int (input('Hoeveel minuten?'))
prijsVR = tijd / 5 * 37
PrijsVR = prijsVR * personen
print('PrijsVR', PrijsVR ,'cent')

Totaal = PrijsToegangtickets + PrijsVR
print('Totaal', Totaal ,'cent')

print(f'Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {tijd} minuten VR kost je maar {Totaal} cent')