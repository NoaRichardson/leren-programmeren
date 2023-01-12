# Deze functie stelt een vraag, valideert en controleert of de input een valide leeftijd is
# Functie vraagt het rgel 3-15 is waar het door heen gaat en er komt een int uit
def vraag_leeftijd_gebruiker(vraag: str) -> int:
    while True:
        leeftijd_string = input(vraag)
        if not leeftijd_string.isnumeric():
            print("Voer een getal in")
        elif int(leeftijd_string) > 130:
            print("Zo oud is nog niemand geworden!")
        elif int(leeftijd_string) < 0:
            print("U bent nog niet geboren")
        else:
            leeftijd = int(leeftijd_string)
            break
    return leeftijd

def vraag_naam_gebruiker(vraag: str):
    naam = input("Hoe heet je?")
    return naam

print("Hallo wereld")
naam = vraag_naam_gebruiker("Hoe heet je?")
leeftijd = vraag_leeftijd_gebruiker("Hoe oud ben je?") 
print(f"Hallo {naam}, je leeftijd is {leeftijd}")