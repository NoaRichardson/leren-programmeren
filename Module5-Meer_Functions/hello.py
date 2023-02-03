def function_1():
    zin = str('Hello from function town')

    return zin

def vraag_hoeveel(vraag: int):
    while True:
        towns_hoeveel = input("Hoeveel towns wil je?")
        if not towns_hoeveel.isnumeric():
            print("Vul een getal in")
        else:
            towns = int(towns_hoeveel)
            break
    return towns

zin = str("Hello from function town")
towns = vraag_hoeveel("Hoeveel towns wil je")

def function_2():
    for x in range(1,towns+1):
        print(f"{zin} {x}!")

function_2()
    



