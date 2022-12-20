import random

namen_list = []
lootjes_list = []
dictonairy = {}
dictlist = []
more_name = 'ja'

while more_name == 'ja':
    name = input('Naam?')
    if name in namen_list:
        name = input('Naam?')
    namen_list.append(name)
    lootjes_list.append(name)
    if len(namen_list) >= 3 :
        more_name = input('Wilt u nog een naam toevoegen?')

while len(namen_list) > 0:
    naam = random.choice(namen_list)
    lootje = random.choice(lootjes_list)
    if naam != lootje:
        dictonairy[naam] = lootje
        namen_list.remove(naam)
        lootjes_list.remove(lootje)

for x, y in dictonairy.items():
    print(x, y)

        
