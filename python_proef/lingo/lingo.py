from lingowords import *
from lingo_function import *
import random

word = random.choice(words)
poging = 5
hoeveel_letter = f"{word[0]}____"
test = ["_", "_", "_", "_", "_"]
print(hoeveel_letter)
print(word)
for x in range(poging):
    guess = try_word()
    green = find_green(word, guess)
    test_list = remove_green(green, word)
    yellow = find_yellow(test_list, guess)
    result_guess = print_guess(green, yellow, guess)
    guessed_right = bijhouden_guess(result_guess, test)
    print("")
    print(''.join(test))