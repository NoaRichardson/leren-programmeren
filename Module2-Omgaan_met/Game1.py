game_1 = "on"
while game_1 == "on":
    woonkamer_deur = 0
    door_sleutel = 0
    game = 1
    kamer = 1
    room_choice = ['het bed', 'de deur', 'het bureau', 'het raam']
    woonkamer_choice = ['het papier', 'het schilderij', 'de boekenkast', 'de deur', 'ga terug']
    def room_check_1():
        while True:
            check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam').lower()
            if check not in room_choice:
                print("Kies een van de keuzes!")
            else:
                break
        return check
    rc_1 = room_check_1()
    def woonkamer_check():
        while True:
            check = input('Wat wil je checken? het papier, het schilderij, de boekenkast, de deur of ga terug').lower()
            if check not in woonkamer_choice:
                print("Kies een van de keuzes!")
            else:
                break
        return check

    while game == 1:
        while kamer == 1 :
            while rc_1 == 'het bed':
                doos = input('Er is een doos onder het bed wil je het proberen te paken?')
                if doos =='ja':
                    print('Het is te zwaar om te verplaatsen')
                    open_doos = input('Wil je proberen de doos te openen?')
                    if open_doos == 'ja':
                        print('Het is opslot je hebt een code nodig')
                        doos_code = input('Code proberen?')
                        if doos_code == 'ja':
                            code = input('')
                            if code == '21744':
                                print('Er zit een sleutel er in')
                                woonkamer_deur = 1
                                rc_1 = room_check_1()
                            else:
                                print('De code is fout')
                        elif doos_code == 'nee':
                            rc_1 = room_check_1()
                    elif open_doos == 'nee':
                        rc_1 = room_check_1()
                elif doos =='nee':
                    rc_1 = room_check_1()

            while rc_1 == 'de deur':
                if door_sleutel == 0 :
                    print('Je hebt een sleutel nodig')
                    rc_1 = room_check_1()
                elif door_sleutel == 1 :
                    kamer = 2
                    break

            while rc_1 == 'het bureau':
                print('Er is een sleutel op het bureau')
                door_sleutel = 1
                rc_1 = room_check_1()

            while rc_1 == 'het raam':
                print('Het is op slot van de andere kant')
                rc_1 = room_check_1()

        while kamer == 2:
            gang = input('Wil je de kamer verlaten?')
            if gang == 'ja':
                RofL = input('Je kan links of rechts gaan welke kant ga je?').lower()
                if RofL == 'rechts':
                    print('De planken breken onder je voeten')
                    print('YOU DIED')
                    exit()
                elif RofL == 'links':
                    print('Je komt in een woonkamer terecht')
                    kamer = 3
            elif gang == 'nee':
                door_sleutel = 0
                room_check = 0
                kamer = 1
        while kamer == 3:
            wkc = woonkamer_check()
            while wkc == 'het papier':
                print('Het is een bon voor 21 boeken')
                break 

            while wkc == 'het schilderij':
                print('Je ziet 2 cijfers in het schilderij 7 en 4')
                break

            while wkc == 'de boekenkast':
                print('Er zijn 4 planken met boeken')
                break

            while wkc == 'de deur':
                if woonkamer_deur == 0:
                    print('Het is op slot je hebt een sleutel nodig')
                    break
                elif woonkamer_deur == 1:
                    print('YOU WIN')
                    game_inp = input("Wil je nog een keer?").lower()
                    if game_inp == "ja":
                        woonkamer_deur = 0
                        door_sleutel = 0
                        game = 1
                        kamer = 1
                    elif game_inp == "nee":
                        quit()
            
            while wkc == 'ga terug':
                door_sleutel = 0
                room_check = 0
                kamer = 1
                break     