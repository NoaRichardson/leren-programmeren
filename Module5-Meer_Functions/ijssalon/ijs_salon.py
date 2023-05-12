from salon_functions import *

order = ""
zaken_order = ""
lijst_smaken_liters = [0, 0, 0, 0]
aantal_hoorntjes = 0
aantal_bakjes = 0
prijs_topping = 0
smaken = []
klant = wat_voor_klant()
if klant == "1":
    print("Welkom bij Papi Gelato.")
    order = "ja"
else:
    zaken_order = "ja"

while order == "ja":
    bollentjes = hoeveel_bollentjes()
    if bollentjes > 8:
        print("Sorry we hebben geen bakjes dat groot.")
    else:
        smaken += wat_voor_smaak(bollentjes)
        if bollentjes < 4:
            ijs_houder = vraag_hoorntje_bakje()
        else:
            ijs_houder = "bakje"

        if ijs_houder == "hoorntje":
            aantal_hoorntjes += 1
        else:
            aantal_bakjes += 1

        bollentje_topping = topping()
        prijs_topping += berekenen_topping(bollentje_topping, bollentjes, ijs_houder)
        order = meer_bestellen(ijs_houder)

while zaken_order == "ja":
    liters = hoeveel_liter()
    smaak_liters = wat_voor_smaak(liters)
    lijst_smaken_liters = aantal_smaken(smaak_liters)
    zaken_order = "nee"


hoorntjes_bakjes = aantal_hoorntjes_bakjes(aantal_hoorntjes, aantal_bakjes)       
aantal_bollentjes_smaken = aantal_smaken(smaken)
bon = berekenen_bon(hoorntjes_bakjes, aantal_bollentjes_smaken, aantal_hoorntjes, aantal_bakjes, prijs_topping, lijst_smaken_liters, zaken_order)
print(bon)