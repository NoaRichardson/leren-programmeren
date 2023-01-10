import random

namen_list = []
lootjes_list = []
lootjes_dict = {}
extra_list = []

more_name = 'ja'

# while more_name == 'ja':
#     while True:
#         name = input('Naam?')
#         if name in namen_list:
#             print('U heeft deze naam al gekozen')
#         else:
#             break
        
#     namen_list.append(name)
#     lootjes_list.append(name)
#     extra_list.append(name)
#     if len(namen_list) >= 3 :
#         more_name = input('Wilt u nog een naam toevoegen?')
for x in range(100):
    namen_list = ['jan', 'piet', 'klaas']
    lootjes_list = ['jan', 'piet', 'klaas']
    extra_list = ['jan', 'piet', 'klaas']
    while len(namen_list) > 0:
        namen_list = [] + extra_list
        lootjes_list = [] + extra_list
        while len(namen_list) > 0:
            naam = random.choice(namen_list)
            lootje = random.choice(lootjes_list)
            if naam != lootje:
                lootjes_dict[naam] = lootje
                namen_list.remove(naam)
                lootjes_list.remove(lootje)
                if len(namen_list) == 0:
                    for x, y in lootjes_dict.items():
                        print(x, y)
            elif naam == lootje:
                break
