def naam_leeftijd(vraag: str)-> list[dict]:
    list_nl = []
    while True:
        naam = input('naam?')
        if naam == 'stop':
            break
        leeftijd = input('leeftijd?')
        if leeftijd == 'stop':
            break
        else:
            list_nl.append({naam : leeftijd})
    return list_nl


list_nl = naam_leeftijd('naam?')
i = 0
for namen in list_nl:
    print(list_nl[i])
    i = i + 1
      