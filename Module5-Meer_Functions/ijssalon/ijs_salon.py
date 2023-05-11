from salon_functions import *

aantal_bollentjes = 0
aantal_hoorntjes = 0
aantal_bakjes = 0
smaken = []
print("Welkom bij Papi Gelato.")

order = "ja"
while order == "ja":
    bollentjes = hoeveel_bollentjes()
    aantal_bollentjes += bollentjes
    if bollentjes > 8:
        print("Sorry we hebben geen bakjes dat groot.")
        aantal_bollentjes =- bollentjes
    else:
        smaken += smaak_bollentjes()
        if bollentjes < 4:
            ijs_houder = vraag_hoorntje_bakje()
            if ijs_houder == "hoorntje":
                aantal_hoorntjes += 1
            else:
                aantal_bakjes += 1
        elif bollentjes >= 4 and bollentjes <= 8:
            ijs_houder = "bakje"
            aantal_bakjes += 1

        order = meer_bestellen(ijs_houder)

hoorntjes_bakjes = aantal_hoorntjes_bakjes(aantal_hoorntjes, aantal_bakjes)       
aantal_bollentjes_smaken = aantal_smaken(smaken)
bon = berekenen_bon(hoorntjes_bakjes, aantal_bollentjes_smaken, aantal_hoorntjes, aantal_bakjes)
print(bon)