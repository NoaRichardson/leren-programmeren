dictboodschap = {}
boodschappen_lijst = []
meer_boodschappen = ""
while meer_boodschappen != "nee":
    boodschap = str(input("Wat wilt u kopen?")).lower()
    aantal_boodschap = int(input("Hoeveel?"))

    if boodschap in dictboodschap:
        dictboodschap[boodschap] += aantal_boodschap
    else:
        dictboodschap[boodschap] = aantal_boodschap

    meer_boodschappen = str(input("Wilt u nog meer kopen?")).lower()
    


print(dictboodschap)


        


