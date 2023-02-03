def naam_leeftijd()-> dict:
    naam = input('naam?')  
    leeftijd = input('leeftijd?')
    
    return {'naam' : naam, 'leeftijd' : leeftijd}


NL_list = []

while True:
    NL = naam_leeftijd()
    if NL['naam'] != 'stop':
        NL_list.append(NL)
    else:
        break
    
print(NL_list)

    