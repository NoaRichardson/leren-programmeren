from random import choice, sample
vorig_compliment = ""

naam = input("Wat is je naam?")
hoeveel_complimenten = int(input("Hoeveel complimenten wil je?"))

compliment_lijst = (f"Je bent geweldig {naam}", f"Je bent goed bezig {naam}", f"Goed gedaan {naam}", f"Je ziet er goed uit {naam}")

for x in range (hoeveel_complimenten):
     compliment = choice(compliment_lijst)
     while compliment == vorig_compliment:
        compliment = choice(compliment_lijst)
     print(compliment)
     vorig_compliment = compliment
     