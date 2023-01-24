def limit(vraag: int):
    while True:
        hoeveel = input('Hoelang wilt u dat de fibonacci door gaat?')
        if not hoeveel.isnumeric():
            print('Vul een getal in!')
        else:
            hoeveel = int(hoeveel)
            break
    return hoeveel
hoeveel = limit(int)

def fibonacci(list) -> list:
    fibonacci_list = [0, 1]
    i = 0
    for x in range(hoeveel):
        getal = fibonacci_list[i] + fibonacci_list[i + 1]
        fibonacci_list.append(getal)
        i = i + 1
    return fibonacci_list
fibonacci_list = fibonacci(list)
print(fibonacci_list)

def gulden_snede(float):
    laatste_getal = len(fibonacci_list) - 1
    snede = fibonacci_list[laatste_getal] / fibonacci_list[laatste_getal - 1]
    return snede
snede = gulden_snede(float)
print(snede)
    