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
     order = input(f"Hier is uw {ijs_houder}. Wilt u nog iets anders bestellen?")
     if order not in ("ja", "nee"):
          print("Sorry dat snap ik niet...")
     else:
          return order
