# Start game intro
while True:
    name_player = input('Wat is je naam?')
    if len(name_player) < 1:
        print("Je moet iets invullen")
    else:
        break
print(f"Welkom {name_player}.")

# Kamer 1 

room_choice = ['het bed', 'de deur', 'het bureau', 'het raam']
room_choice_3 = ['het papier', 'het schilderij', 'de boekenkast', 'de deur', 'ga terug']
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
            print('')
            room_check_1()
        else:
           room_check_1()
    else:
        room_check_1()

def de_deur():
    ant_deur = input("Wil je naar de andere kamer?").lower()
    if ant_deur == 'ja':
        room_check_2()
    elif ant_deur == 'nee':
        room_check_1()

def het_bureau():
    print("Op het bureau staat 2314")
    room_check_1()

def het_raam():
    print("Het is op slot van de andere kant")
    room_check_1()

# Kamer 2

def room_check_2():
    welke_kant = input("Je bent in een gang welke kant ga je op?\n links, rechts of terug?").lower()
    if welke_kant == "rechts":
        print("De planken breken onder je voeten")
        print("YOU DIED")
        quit()
    elif welke_kant == "links":
        room_check_3()
    elif welke_kant == "terug":
        room_check_1()

# Kamer 3

def room_check_3():
    while True:
        check_2 = input("Wat wil je checken? het papier, het schilderij, de boekenkast, de deur of ga terug")
        if check_2 not in room_choice_3:
            print("kies een van de keuzes!")
        else:
            break
    return check_2




# Er zit hier een probleem met de check hij doet bij sommige niks maar het ligt aan welke volgorde je kiest
check = room_check_1()
if check == 'het bed':
    het_bed()
elif check == 'de deur':
    de_deur()
elif check == 'het bureau':
    het_bureau()
elif check == 'het raam':
    het_raam()