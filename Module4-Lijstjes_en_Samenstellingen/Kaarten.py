import random

deck = []
kaarten = ["harten", "klaveren", "schoppen", "ruiten"]
nummers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]

for kaart in kaarten:
    for num in nummers:
        deck.append(f"{kaart}  {num}")

deck.append("joker")
deck.append("joker")
random.shuffle(deck)

pop = 0
i = 1
for x in range(7):
    bovenste = deck.pop(pop)
    print(f"kaart{i} = {bovenste}")
    pop = pop + 1
    i = i + 1

print(deck)


    

