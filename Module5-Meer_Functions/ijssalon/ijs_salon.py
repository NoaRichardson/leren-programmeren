from salon_functions import *

print("Welkom bij Papi Gelato je mag alle smaken kiezen zoland het maar vanille is.")

order = "ja"
while order == "ja":
    bollentjes = hoeveel_bollentjes()
    if bollentjes < 4:
        ijs_houder = HofB()
        order = input(f"Hier is u {ijs_houder}. Wilt u nog iets anders bestellen?")
    elif bollentjes >= 4 and bollentjes <= 8:
        ijs_houder = "bakje"
        order = input(f"Hier is u {ijs_houder}. Wilt u nog iets anders bestellen?")
    elif bollentjes > 8:
        print("Sorry we hebben geen bakjes dat groot.")

print("Bedankt en tot ziens.")