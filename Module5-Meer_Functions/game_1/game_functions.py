def room_check_1():
    ROOM_CHOICE = ['het bed', 'de deur', 'het bureau', 'het raam']
    while True:
        check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam').lower()
        if check not in ROOM_CHOICE:
            print("Kies een van de keuzes!")
        else:
            break
    return check

def het_bed():
    ant_bed = input('Er zit een kluis onder het bed om het te openen\n Heb je een code nodig wile je de code proberen?').lower()
    if ant_bed == 'ja':
        try_code_bed = input("code:")
        return try_code_bed

def de_deur():
    ant_deur = input("Wil je naar de andere kamer?").lower()
    return ant_deur


# Kamer 2

def room_check_2():
    ROOM_CHOICE_2 = ['links', 'rechts', 'terug']
    while True:
        welke_kant = input("Je bent in een gang welke kant ga je op?\n links, rechts of terug?").lower()
        if welke_kant not in ROOM_CHOICE_2:
            print("Kies een van de keuzes!")
        else:
            break
    return welke_kant

# Kamer 3

def room_check_3():
    ROOM_CHOICE_3 = ['het papier', 'het schilderij', 'de boekenkast', 'de deur', 'ga terug']
    while True:
        check_2 = input("Wat wil je checken? het papier, het schilderij, de boekenkast, de deur of ga terug").lower()
        if check_2 not in ROOM_CHOICE_3:
            print("kies een van de keuzes!")
        else:
            break
    return check_2

def de_deur_2():
    code_deur = input("Je hebt een code nodig om de deur te openen.\n Wil je het proberen?")
    if code_deur == 'ja':
        deur_2 = True
        return deur_2
    else:
        deur_2 = False
        return code_deur

def de_deur_2_2():
    try_deur = input('Code:')
    return try_deur