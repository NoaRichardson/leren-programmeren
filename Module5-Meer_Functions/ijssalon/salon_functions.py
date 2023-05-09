def hoeveel_bollentjes():
    while True:
        hoeveel = input("Hoeveel bollentjes wilt u?")
        if hoeveel.isnumeric:
            return int(hoeveel)
        else:
            print("Sorry dat snap ik niet...")

def HofB():
    while True:
        KIES_LIJST = "hoortje", "bakje"
        hofb = input("Wilt u dat in een hoortje of bakje?")
        if hofb in KIES_LIJST:
                return hofb
        else:
            print("Sorry dat snap ik niet...")