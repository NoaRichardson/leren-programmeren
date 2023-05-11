from salon_functions import *

aantal_bollentjes = 0
aantal_hoorntjes = 0
aantal_bakjes = 0
print("Welkom bij Papi Gelato je mag alle smaken kiezen zoland het maar vanille is.")

order = "ja"
while order == "ja":
    bollentjes = hoeveel_bollentjes()
    aantal_bollentjes += bollentjes
    if bollentjes > 8:
        print("Sorry we hebben geen bakjes dat groot.")
        aantal_bollentjes =- bollentjes
    else:
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

salon_bon = bon(aantal_bollentjes, aantal_hoorntjes, aantal_bakjes)       
print("---------Papi Gelato---------")
if aantal_bollentjes > 0:
    print(f"Bollentjes   {aantal_bollentjes} x $1,10 = {salon_bon[0]}")
if aantal_hoorntjes > 0:
    print(f"Hoorntjes   {aantal_hoorntjes} x $1,25 = {salon_bon[1]}")
if aantal_bakjes > 0:
    print(f"Bakjes   {aantal_bakjes} x $0,75 = {salon_bon[2]}")
print("Bedankt en tot ziens!")