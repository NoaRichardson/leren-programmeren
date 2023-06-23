class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# 1 Find the green and remove from copy list and put in other list
# 2 Find yellow remove from copy list put with green in order
# 3 Print the colors right

def try_word():
    while True:
        guess = input("Raad:")
        if len(guess) > 5:
            print("Alle woorden zijn maar 5 letters lang")
        elif len(guess) < 5:
            print("Alle woorden zijn 5 letters lang")
        else:
            return guess
        
def find_green(word, guess):
    list_green = []
    index = 0
    for letter in word:
        if guess[index] == word[index]:
            list_green.append(letter)
            index += 1
        else:
            list_green.append("_")
            index += 1
    return list_green

def remove_green(green, word):
    list_no_green = []
    index = 0
    for letter in word:
        if letter == green[index]:
            list_no_green.append("_")
            index += 1
        else:
            list_no_green.append(letter)
            index += 1
    return list_no_green

def find_yellow(test_list, guess):
    yellow = []
    for letter in guess:
        if letter in test_list:
            yellow.append(letter)
            test_list.remove(letter)
        else:
            yellow.append("_")
    return yellow

def print_guess(green, yellow, guess):
    index = 0
    result_guess = []
    for letter in guess:
        if letter == green[index]:
            print(bcolors.OKGREEN + f"{letter}" + bcolors.ENDC, end="")
            result_guess.append(letter)
            index += 1
        elif letter == yellow[index]:
            print(bcolors.WARNING + f"{letter}" + bcolors.ENDC, end="")
            result_guess.append("_")
            index += 1
        else:
            print("_", end="")
            result_guess.append("_")
            index += 1
    return result_guess

def bijhouden_guess(result_guess, test):
    guessed = []
    index = 0
    for letter in test:
        if letter != "_":
            guessed.append(letter)
            index += 1
        elif result_guess[index] != "_":
            guessed.append(result_guess[index])
    return guessed