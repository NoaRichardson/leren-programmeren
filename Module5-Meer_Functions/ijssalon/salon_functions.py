def hoeveel_bollentjes():
    while True:
        hoeveel = input("Hoeveel bollentjes wilt u?")
        if hoeveel.isnumeric:
            return int(hoeveel)
        else:
            print("Sorry dat snap ik niet...")

def vraag_hoorntje_bakje():
    while True:
        KIES_LIJST = "hoorntje", "bakje"
        hofb = input("Wilt u dat in een hoorntje of bakje?")
        if hofb in KIES_LIJST:
                return hofb
        else:
            print("Sorry dat snap ik niet...")

def meer_bestellen(ijs_houder):
     while True:
        order = input(f"Hier is uw {ijs_houder}. Wilt u nog iets anders bestellen?")
        if order not in ("ja", "nee"):
            print("Sorry dat snap ik niet...")
        else:
            return order
     
def bon(aantal_bollentjes, aantal_hoorntjes, aantal_bakjes):
     prijs_bollentjes = round(aantal_bollentjes * 1.10, 2)
     prijs_hoorntjes = round(aantal_hoorntjes * 1.25, 2)
     prijs_bakjes = round(aantal_bakjes * 0.75, 2)
     return prijs_bollentjes, prijs_hoorntjes, prijs_bakjes
