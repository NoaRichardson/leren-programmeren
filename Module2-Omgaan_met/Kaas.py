#Kaas.py

print('Als je antwoord ja is type je 1 als je antwoord nee is type je 2')
ant = int(input('Is de kaas geel?'))

#ja =1 nee =2
ka = 1

if ka == ant :
    ant = int (input('Zitten er gaten in?'))
    if ka == ant :
        ant = int(input('Is de kaas belagelijk duur?'))
        if ka == ant :
            print('Emmenthaler')
        elif ka < ant :
            print('Leerdammer') 
            
    elif ka < ant :
     ant = int(input('Is de kaas hard als steen?'))
     if ka == ant :
            print('Parmigiano Reggiano')
     elif ka < ant :
        print('Goudse Kaas')

         

elif ka < ant :
    ant = int(input('Heeft de kaas blauwe schimmel?'))
    if ka == ant :
        ant = int(input('Heeft de kaas korst?'))
        if ka == ant :
            print('Blue de Rochbaron')
        elif ka < ant :
            print('Foume d Ambert')
    elif ka < ant :
        ant = int(input('Heeft de kaas korst?'))
        if ka == ant :
            print('Camembert')
        if ka < ant :
            print('Mozzarella')
     








