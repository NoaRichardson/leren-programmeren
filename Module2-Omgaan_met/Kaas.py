#Kaas.py

geel = input('Is de kaas geel?')

if geel == 'ja':
    gaten = input('Zitten er gaten in?')
    if gaten == 'ja':
        duur = input('Is de kaas belagelijk duur?')
        if duur == 'ja':
            print('Emmenthaler')
        elif duur == 'nee':
            print('Leerdammer') 
            
    elif gaten == 'nee':
     steen = input('Is de kaas hard als steen?')
     if steen == 'ja':
            print('Parmigiano Reggiano')
     elif steen == 'nee':
        print('Goudse Kaas')

         

elif geel == 'nee':
    schimmel = input('Heeft de kaas blauwe schimmel?')
    if schimmel == 'ja':
        korst = input('Heeft de kaas korst?')
        if korst == 'ja':
            print('Blue de Rochbaron')
        elif korst == 'nee':
            print('Foume d Ambert')
    elif schimmel == 'nee':
        korst = input('Heeft de kaas korst?')
        if korst == 'ja':
            print('Camembert')
        if korst == 'nee':
            print('Mozzarella')
     








