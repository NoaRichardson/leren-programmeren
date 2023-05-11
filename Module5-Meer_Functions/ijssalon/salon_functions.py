def hoeveel_bollentjes():
    while True:
        hoeveel = input("Hoeveel bollentjes wilt u?")
        if hoeveel.isnumeric() and int(hoeveel) > 0:
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
     
def aantal_hoorntjes_bakjes(aantal_hoorntjes, aantal_bakjes):
     prijs_hoorntjes = round(aantal_hoorntjes * 1.25, 2)
     prijs_bakjes = round(aantal_bakjes * 0.75, 2)
     return prijs_hoorntjes, prijs_bakjes

def wat_voor_smaak(bollentjes):
    lijst_smaak = []
    while True:
        for ijs in range(0, bollentjes):
            smaak = input("Welke smaak wilt u?\nA)Aardbei\nC)Chocolade\nM)Munt\nV)Vanille\nSmaak:")
            if smaak not in ("a", "c", "m", "v"):
                print("Sorry dat snap ik niet...")
            else:
                lijst_smaak.append(smaak)
        return lijst_smaak

def aantal_smaken(smaken):
    aarbei = 0
    chocolade = 0
    munt = 0
    vanilla = 0
    for i in smaken:
        if i == "a":
            aarbei += 1
        elif i == "c":
            chocolade += 1
        elif i == "m":
            munt += 1
        elif i == "v":
            vanilla += 1
    return aarbei, chocolade, munt, vanilla

def topping():
    while True:
        welke_topping = input("Wat voor topping wilt u?\nA)geen\nB)slagroom\nC)sprinkels\nD)caramel saus\nTopping:")
        if welke_topping not in ("a", "b", "c", "d"):
            print("Sorry dat begrijp ik niet...")
        else:
            return welke_topping
        
def berekenen_topping(bollentje_topping, bollentjes, ijs_houder):
    if bollentje_topping == "a":
        prijs_topping = 0
    elif bollentje_topping == "b":
        prijs_topping = 0.50
    elif bollentje_topping == "c":
        prijs_topping = bollentjes * 0.30
    else:
        if ijs_houder == "hoorntje":
            prijs_topping = 0.60
        else:
            prijs_topping = 0.90
    return prijs_topping


def berekenen_bon(hoorntjes_bakjes, aantal_bollentjes_smaken, aantal_hoorntjes, aantal_bakjes, prijs_topping, lijst_smaken_liters, zaken_order):
    totaal = 0
    bon = "---------Papi Gelato---------\n"
    if aantal_bollentjes_smaken[0] > 0:
        a_totaal = round(aantal_bollentjes_smaken[0] * 1.10, 2)
        bon += f"B.Aardbei    {aantal_bollentjes_smaken[0]} x $1,10 = {a_totaal}\n"
        totaal += a_totaal
    if aantal_bollentjes_smaken[1] > 0:
        c_totaal = round(aantal_bollentjes_smaken[1] * 1.10, 2)
        bon += f"B.Chocolade  {aantal_bollentjes_smaken[1]} x $1,10 = {c_totaal}\n"
        totaal += c_totaal
    if aantal_bollentjes_smaken[2] > 0:
        m_totaal = round(aantal_bollentjes_smaken[2] * 1.10, 2)
        bon += f"B.Munt       {aantal_bollentjes_smaken[2]} x $1,10 = {m_totaal}\n"
        totaal += m_totaal
    if aantal_bollentjes_smaken[3] > 0:
        v_totaal = round(aantal_bollentjes_smaken[3] * 1.10, 2)
        bon += f"B.Vanille    {aantal_bollentjes_smaken[3]} x $1,10 = {v_totaal}\n"
        totaal += v_totaal
    if aantal_hoorntjes > 0:
        bon += f"Hoorntje     {aantal_hoorntjes} x $1.25 = {hoorntjes_bakjes[0]}\n"
        totaal += hoorntjes_bakjes[0]
    if aantal_bakjes > 0:
        bon += f"Bakjes       {aantal_bakjes} x &0.75 = {hoorntjes_bakjes[1]}\n"
        totaal += hoorntjes_bakjes[1]
    if prijs_topping > 0:
        bon += f"Topping                 {prijs_topping}\n"
        totaal += prijs_topping
    # Berekeningen voor zaken klanten.
    if lijst_smaken_liters[0] > 0:
        bon += f"L.Aardbei      {lijst_smaken_liters[0]} x 9.80 = {round(lijst_smaken_liters[0] * 9.80, 2)}\n"
        totaal += lijst_smaken_liters[0] * 9.80
    if lijst_smaken_liters[1] > 0:
        bon += f"L.Chocolade    {lijst_smaken_liters[1]} x 9.80 = {round(lijst_smaken_liters[1] * 9.80, 2)}\n"
        totaal += lijst_smaken_liters[1] * 9.80
    if lijst_smaken_liters[2] > 0:
        bon += f"L.Munt         {lijst_smaken_liters[2]} x 9.80 = {round(lijst_smaken_liters[2] * 9.80, 2)}\n"
        totaal += lijst_smaken_liters[2] * 9.80
    if lijst_smaken_liters[3] > 0:
        bon += f"L.Vanilla      {lijst_smaken_liters[3]} x 9.80 = {round(lijst_smaken_liters[3] * 9.80, 2)}\n"
        totaal += lijst_smaken_liters[3] * 9.80

    bon += f"Totaal                  {round(totaal, 2)}\n"
    if zaken_order == "nee":
        bon += f"BTW(9%)                 {round(totaal/100 * 9, 2)}"
    return bon

def wat_voor_klant():
    while True:
        kies_wat_voor_klant = input("Bent u 1) een particuliere klant of 2) een zakelijke klant?")
        if kies_wat_voor_klant not in ("1", "2"):
            print("Sorry dat snap ik niet...")
        else:
            return kies_wat_voor_klant
    
def hoeveel_liter():
    while True:
        hoeveelheid_liter = input("Hoeveel liter wilt u?")
        if hoeveelheid_liter.isnumeric() and int(hoeveelheid_liter) > 0:
            return int(hoeveelheid_liter)
        else:
            print("Sorry dat snap ik niet...")