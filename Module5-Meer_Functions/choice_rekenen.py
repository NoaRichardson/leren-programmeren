choice_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
firstRound = True
n1 = False
n2 = False
rekenmachine = True
while rekenmachine:
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

    while True:
        choice = input('Wat wil je doen?\n A) getallen optellen,\n B) getallen aftrekken,\n C) getallen vermenigvuldigen,\n D) getallen delen,\n E) getal ophogen,\n F) getal verlagen,\n G) getal verdubbelen of\n H) getal halveren?\n').upper()
        if choice == '':
            if firstRound == False:
                quit()
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

    while True:
        if n1 == False:
            n1 = input('Kies een getal')
            if not n1.isnumeric():
                print('Dat is geen getal')
                n1 = False
        elif n2 == False:
            n2 = input('Kies een getal')
            if not n2.isnumeric():
                print('Dat is geen getal')
                n2 = False
        else:
            n1 = float(n1)
            n2 = float(n2)
            break

    if choice == 'A' or choice == 'E':
        print(f'{n1} + {n2} = {optellen(n1, n2)}')
        n1 = n1 + n2
    elif choice == 'B' or choice == 'F':
        print(f'{n1} - {n2} = {aftrekken(n1, n2)}')
        n1 = n1 - n2
    elif choice == 'C' or choice == 'G':
        print(f'{n1} x {n2} = {vermenigvuldigen(n1, n2)}')
        n1 = n1 * n2
    elif choice == 'D' or choice == 'H':
        print(f'{n1} : {n2} = {delen(n1, n2)}')
        n1 = n1 / n2
    
    n2 = False
    firstRound = False
    