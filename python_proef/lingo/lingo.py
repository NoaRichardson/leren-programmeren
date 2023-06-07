from lingowords import *
from lingo_function import *
import random

word = random.choice(words)
poging = 5
hoeveel_letter = f"{word[0]} _ _ _ _"
print(hoeveel_letter)
print(word)
result_string = ["_", "_", "_", "_", "_"]
for x in range(poging):
    try_word = poging_raden(word)
    result_try = hoeveel_juist(try_word, word)
    for position in range(len(result_try)):
        if result_try[position] != "_":
            result_string[position] = result_try[position]
    print (f"\n{''.join(result_string)}")
    if result_try == word:
        print(bcolors.OKGREEN + "Je hebt het geraden!" + bcolors.ENDC)
        break

if result_try != word:
    print(word)