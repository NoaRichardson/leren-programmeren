#Kaas.py

print('Als je antwoord ja is type je 1 als je antwoord nee is type je 2')
ant = input('Is de kaas geel?')

if ant == 'ja':
    ant2 = input('Zitten er gaten in?')
    if ant2 == 'ja':
        ant3 = input('Is de kaas belagelijk duur?')
        if ant3 == 'ja':
            print('Emmenthaler')
        elif ant3 == 'nee':
            print('Leerdammer') 
            
    elif ant2 == 'nee':
     ant4 = str(input('Is de kaas hard als steen?'))
     if ant4 == 'ja':
            print('Parmigiano Reggiano')
     elif ant4 == 'nee':
        print('Goudse Kaas')

         

elif ant == 'nee':
    ant5 = input('Heeft de kaas blauwe schimmel?')
    if ant5 == 'ja':
        ant6 = input('Heeft de kaas korst?')
        if ant6 == 'ja':
            print('Blue de Rochbaron')
        elif ant6 == 'nee':
            print('Foume d Ambert')
    elif ant5 == 'nee':
        ant7 = input('Heeft de kaas korst?')
        if ant7 == 'ja':
            print('Camembert')
        if ant7 == 'nee':
            print('Mozzarella')
     








