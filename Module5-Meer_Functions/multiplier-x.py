def keer_som(vraag: int):
    tafel = ""
    for x in range(1,11):
        tafel += f'{x} x {nummer} = {x * nummer}\n'
    return tafel

nummer = int(input("Welke tafel wilt u zien?"))
print(keer_som(nummer))
