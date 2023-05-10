from salon_functions import *

print("Welkom bij Papi Gelato je mag alle smaken kiezen zoland het maar vanille is.")

order = "ja"
while order == "ja":
    bollentjes = hoeveel_bollentjes()
    if bollentjes > 8:
        print("Sorry we hebben geen bakjes dat groot.")
    else:
        if bollentjes < 4:
            ijs_houder = vraag_hoorntje_bakje()
        elif bollentjes >= 4 and bollentjes <= 8:
            ijs_houder = "bakje"

        order = meer_bestellen(ijs_houder)
        
print("Bedankt en tot ziens.")