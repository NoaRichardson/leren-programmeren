iteraties = 0

while True:
    vraag = input("?")
    iteraties = iteraties + 1
    if vraag == "quit":
        print(f"De vraag is {iteraties} keer gesteld")
        break