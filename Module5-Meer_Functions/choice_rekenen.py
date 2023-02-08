def optellen(n1, n2):
    optellen = n1 + n2
    return optellen
def aftrekken(n1, n2):
    aftrekken = n1 - n2
    return aftrekken
def vermenigvuldigen(n1, n2):
    vermedigvuldigen = n1 * n2
    return vermedigvuldigen
def delen(n1, n2):
    delen = n1 / n2
    return delen

def getfloat():
    while True:
        try:
            nummer = input('Kies getal')
            nummer = float(nummer)
            return nummer
        except:
            print('Dat is geen getal!')
        
choice_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
firstRound = True
n1 = False
n2 = False
rekenmachine = True

while rekenmachine:
    while True:
        choice = input('Wat wil je doen?\n A) getallen optellen,\n B) getallen aftrekken,\n C) getallen vermenigvuldigen,\n D) getallen delen,\n E) getal ophogen,\n F) getal verlagen,\n G) getal verdubbelen of\n H) getal halveren?\n').upper()
        if choice == '':
            if firstRound == False:
                rekenmachine = False
        elif choice not in choice_list:
            print('Dat is geen keuze!')
        else:
            break

    if choice == 'E' or choice == 'F':
        n2 = 1
    elif choice == 'G' or choice == 'H':
        n2 = 2
    else:
        n2 = False

    if n1 == False:
        n1 = getfloat()
    if n2 == False:
        n2 = getfloat()

    if choice == 'A' or choice == 'E':
        print(f'{n1} + {n2} = {optellen(n1, n2)}')
        n1 = optellen(n1, n2)
    elif choice == 'B' or choice == 'F':
        print(f'{n1} - {n2} = {aftrekken(n1, n2)}')
        n1 = aftrekken(n1, n2)
    elif choice == 'C' or choice == 'G':
        print(f'{n1} x {n2} = {vermenigvuldigen(n1, n2)}')
        n1 = vermenigvuldigen(n1, n2)
    elif choice == 'D' or choice == 'H':
        print(f'{n1} : {n2} = {delen(n1, n2)}')
        n1 = delen(n1, n2)
    
    
    n2 = False
    firstRound = False
    