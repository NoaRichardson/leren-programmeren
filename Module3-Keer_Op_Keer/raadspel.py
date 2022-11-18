import random
score = 0
teller = 0
round = 0
getal = random.randint(1, 1000)
start = input("Wilt u het spel beginnen?")
print(getal)
while start == "ja":
    raden = 0
    raden = int(input("Raad het getal"))
    verschil = abs(getal - raden)
    if raden == getal:
        print("Je hebt het geraden!")
        score = score + 1
        round = round + 1
        print(score) 
        start = ""
    elif verschil < 20:
        print("Je bent heel warm")
        teller = teller + 1
    elif verschil < 50:
        print("Je bent warm")
        teller = teller + 1
    elif teller == 10:
        print("Je hebt de ronde verloren :(")
        round = round + 1
        print(score)
        start = ""
    else:
        teller = teller + 1
start = input("Wil je nog eens raden?")
if start == "nee":
    print(f"Totale score = {score}")
if round == 20:
    print(f"Totale score = {score}")



