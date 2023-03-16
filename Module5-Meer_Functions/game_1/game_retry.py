from game_functions import *

# Start game intro
while True:
    name_player = input('Wat is je naam?')
    if len(name_player) < 1:
        print("Je moet iets invullen")
    else:
        break
print(f"Welkom {name_player}.")

#Control code

game = ""
room = 1
while game != 'won':
    while room == 1:
        check = room_check_1()
        if check == 'het bed':
            bed = het_bed()
            if bed == '74214':
                print('Er is een briefje met 1212 op')
        elif check == 'de deur':
            ant_deur = de_deur()
            if ant_deur == 'ja':
                room = 2
            else:
                room_check_1
        elif check == 'het bureau':
            print("Op het bureau staat 213")
        elif check == 'het raam':
            print("Het is op slot van de andere kant")
        
    while room == 2:
        RofL = room_check_2()
        if RofL == 'rechts':
            print('De planken breken onder je voeten.\n You Died')
            quit()
        elif RofL == 'links':
            room = 3
        elif RofL == 'terug':
            room = 1
            
    while room == 3:
        check_2 = room_check_3()
        if check_2 == 'het papier':
            print("Het is een bon van 21 boeken")
        elif check_2 == 'het schilderij':
            print('Je ziet 2 cijfers in het schilderij 7 en 4')
        elif check_2 == 'de boekenkast':
            print('Er zijn 4 planken met boeken')
        elif check_2 == 'ga terug':
            room = 2

        elif check_2 == 'de deur':
            code_deur = de_deur_2()
            if code_deur == True:
                try_code_deur = de_deur_2_2()
                if try_code_deur == '1212':
                    print('You win')
                    game = 'won'
                    room = 1
                else:
                    print('De code is incorrect')
            else:
                print('')