dagen = ('Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag')
print("Alle dagen van de week zijn:", dagen[0:6])
print("De werk dagen zijn:", dagen[0:5])
print("Alle weekenddagen zijn:", dagen[5:7])
x = 0, 1, 2, 3, 4
dagenR = reversed(dagen)
dagenR = tuple(dagenR)
print("De werkdgen omgekeerd zijn:", dagenR[2:7])
print("De weekenddagen omgekeerd zijn:", dagenR[0:2])