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

def poging_raden(word):
    while True:
        try_word = input("Raad: ")
        if len(try_word) > 5:
            print("Alle woorden zijn maar 5 letters lang")
        else:
            return try_word
        
# def hoeveel_juist(try_word, word):
#     how_many_right = ""
#     i = 0
#     test_x = 0
#     for letter in try_word:
#         x = word.count(letter)
#         if letter == word[i]:
#             print(bcolors.OKGREEN + f"{letter}" + bcolors.ENDC, end="")
#             how_many_right += f"{letter}"
#             i += 1
#             test_x += 1
#         elif letter in word:
#             if test_x <= x:
#                 print(bcolors.WARNING + f"{letter}" + bcolors.ENDC, end="")
#                 how_many_right += "_"
#                 i += 1
#                 test_x += 1
#             else:
#                 print(bcolors.FAIL + f"{letter}" + bcolors.ENDC, end="")
#                 how_many_right += "_"
#                 i += 1
#         else:
#             print(bcolors.FAIL + f"{letter}" + bcolors.ENDC, end="")
#             how_many_right += "_"
#             i += 1
#     return how_many_right
def hoeveel_juist(try_word, word):
    how_many_right = []
    index = 0
    for letter in try_word:
        if letter == word[index]:
            print(bcolors.OKGREEN + f"{letter}" + bcolors.ENDC, end="")
            index += 1
        else:
            print("_", end="")
            index += 1
    return how_many_right