from fruitmand import fruitmand
import random


aantal_fruit = int(input("Hoeveel stukken fruit?"))
for x in range(aantal_fruit):
      random_fruit = random.choice(fruitmand)
      print(random_fruit['name'])
