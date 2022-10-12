begin = input('Wil je de game beginnen?')
woonkamer_deur = 0
door_sleutel = 0
game = 1
kamer = 1

room_check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam')
while game == 1:
    while kamer == 1 :
        while room_check == 'het bed':
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
                            room_check = 0
                        else:
                            print('De code is fout')
                            room_check = 0
                    elif doos_code == 'nee':
                        room_check = 0
                elif open_doos == 'nee':
                    room_check = 0
            elif doos =='nee':
                room_check = 0

        if room_check == 0:
                room_check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam')

        while room_check == 'de deur':
            if door_sleutel == 0 :
                print('Je hebt een sleutel nodig')
                room_check = 0 
            elif door_sleutel == 1 :
                kamer = 2
                break

        if room_check == 0:
                room_check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam')

        while room_check == 'het bureau':
            print('Er is een sleutel op het bureau')
            door_sleutel = 1
            room_check = 0

        if room_check == 0:
                room_check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam')

        while room_check == 'het raam':
            print('Het is op slot van de andere kant')
            room_check = 0

        if room_check == 0:
                room_check = input('Je bent in een kamer wat wilt u checken? het bed, de deur ,het bureau, het raam')


    while kamer == 2:
        gang = input('Wil je de kamer verlaten?')
        if gang == 'ja':
            RofL = input('Je kan links of rechts gaan welke kant ga je?')
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
        woonkamer_check = input('Wat wil je checken? het papier op de grond, het schilderij, de boekenkast, de deur of ga terug')

        while woonkamer_check == 'het papier op de grond':
            print('Het is een bon voor 21 boeken')
            woonkamer_check = 0

        if woonkamer_check == 0:
            woonkamer_check = input('Wat wil je checken? het papier op de grond, het schilderij, de boekenkast, de deur of ga terug')  

        while woonkamer_check == 'het schilderij':
            print('Je ziet 2 cijfers in het schilderij 7 en 4')
            woonkamer_check = 0

        while woonkamer_check == 'de boekenkast':
            print('Er zijn 4 planken met boeken')
            woonkamer_check = 0

        while woonkamer_check == 'de deur':
            if woonkamer_deur == 0:
                print('Het is op slot je hebt een sleutel nodig')
                woonkamer_check = 0
            elif woonkamer_deur == 1:
                print('YOU WIN')
                exit()
        
        while woonkamer_check == 'ga terug':
            door_sleutel = 0
            room_check = 0
            kamer = 1
            break


        
        
          
          
            

            


            