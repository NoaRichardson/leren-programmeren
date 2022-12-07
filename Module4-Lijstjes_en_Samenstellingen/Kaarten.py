import random

deck = []
kaarten = ("harten", "klaveren", "schoppen", "ruiten")
nummers = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")

for kaart in kaarten:
    for num in nummers:
        deck.append(f"{kaart}  {num}")

deck.append("joker1")
deck.append("joker2")
random.shuffle(deck)

pop = 0
for x in range(1, 8, 1):
    bovenste = deck.pop(pop)
    print(f"kaart{x} = {bovenste}")
    

print(deck)


    

