dictboodschap = {}
boodschappen_lijst = []
meer_boodschappen = ""
while meer_boodschappen != "nee":
    boodschap = str(input("Wat wilt u kopen?"))
    boodschap = boodschap.lower()
    aantal_boodschap = int(input("Hoeveel?"))
    boodschappen_lijst.append(boodschap)

    for spullen in boodschappen_lijst:
        dictboodschap[boodschap] = aantal_boodschap

    meer_boodschappen = str(input("Wilt u nog meer kopen?"))
    if meer_boodschappen == "ja":
        meer_boodschappen = "ja"
    else:
        meer_boodschappen = "nee"
    



print(dictboodschap)


        


