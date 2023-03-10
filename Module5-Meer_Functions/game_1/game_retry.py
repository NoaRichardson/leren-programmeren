# Start game intro
while True:
    name_player = input('Wat is je naam?')
    if len(name_player) < 1:
        print("Je moet iets invullen")
    else:
        break
print(f"Welkom {name_player}.")

# Room Choice

room_choice = ['het bed', 'de deur', 'het bureau', 'het raam']
room_choice_3 = ['het papier', 'het schilderij', 'de boekenkast', 'de deur', 'ga terug']

# Kamer 1

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
        if try_code_bed == "74214":
            print('Er is een briefje met 1212 op')
            room_check_1()
        else:
           room_check_1()
    else:
        room_check_1()

def de_deur():
    ant_deur = input("Wil je naar de andere kamer?").lower()
    return ant_deur

def het_bureau():
    print("Op het bureau staat 213")
    room_check_1()

def het_raam():
    print("Het is op slot van de andere kant")
    room_check_1()

# Kamer 2

def room_check_2():
    welke_kant = input("Je bent in een gang welke kant ga je op?\n links, rechts of terug?").lower()
    return welke_kant

# Kamer 3

def room_check_3():
    while True:
        check_2 = input("Wat wil je checken? het papier, het schilderij, de boekenkast, de deur of ga terug").lower()
        if check_2 not in room_choice_3:
            print("kies een van de keuzes!")
        else:
            break
    return check_2

def de_deur_2():
    code_deur = input("Je hebt een code nodig om de deur te openen.\n Wil je het proberen?")
    if code_deur == 'ja':
        try_code_deur = input("Code:")
        return try_code_deur

#Control code

game = ""
room = 1
while game != 'won':
    while room != 1:
        check = room_check_1()
        if check == 'het bed':
            het_bed()
        elif check == 'de deur':
            ant_deur = de_deur()
            if ant_deur == 'ja':
                room = 2
            else:
                room_check_1
        elif check == 'het bureau':
            het_bureau()
        elif check == 'het raam':
            het_raam()
        
    while room == 2:
        RofL = room_check_2()
        if RofL == 'recht':
            print('De planken breken onder je voeten.\n You Died')
            quit()
        elif RofL == 'links':
            room = 3
        elif RofL == 'terug':
            room = 1
        else:
            print('Kies een van de keuzes!')
            
    while room == 3:
        check_2 = room_check_3()
        if check_2 == 'het papier':
            print("Het is een bon van 21 boeken")
        elif check_2 == 'het schilderij':
            print('Je ziet 2 cijfers in het schilderij 7 en 4')
        elif check_2 == 'de boekenkast':
            print('Er zijn 4 planken met boeken')
        elif check_2 == 'de deur':
            try_code_deur = de_deur_2()
            if try_code_deur == "1212":
                print('You Win!!!')
                game = 'won'
            else:
                print("De code is incorrect")