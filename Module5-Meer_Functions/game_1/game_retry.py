# Start game intro
while True:
    name_player = input('Wat is je naam?')
    if len(name_player) < 1:
        print("Je moet iets invullen")
    else:
        break
# Kamer 1 
room_choice = ['het bed', 'de deur', 'het bureau', 'het raam']
key_1 = False
key_2 = False
def room_check_1():
    while True:
        check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam').lower()
        if check not in room_choice:
            print("Kies een van de keuzes!")
        else:
            break
    return check

def het_bed():
    ant_bed = input('Er zit een kluis onder het bed om het te openen\n Heb je een code nodig wile je de code proberen?').lower()
    if ant_bed == 'ja':
        try_code_bed = input("code:")
        if try_code_bed == "21744":
            key_2 = True
            room_check_1()
        else:
           room_check_1()
    else:
        room_check_1()

def de_deur():
    if key_1 == False:
        print("Je hebt een sleutel nodig")
        room_check_1()
    elif key_1 == True:
        print('placeholder.')

def het_bureau():
    if key_1 == False:
        print("Er is een sleutel op het bureau")
        room_check_1()
    else:
        print("Er is niks anders op het bureau")
        room_check_1()

def het_raam():
    print("Het is op slot van de andere kant")
    room_check_1()

check = room_check_1()
if check == 'het bed':
    het_bed()
if check == 'de deur':
    de_deur()
if check == 'het bureau':
    het_bureau()
if check == 'het raam':
    het_raam()
