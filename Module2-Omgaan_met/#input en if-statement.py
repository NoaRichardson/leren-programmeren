#input en if-statement


a = int(input('Wat is a ='))
b = int(input('Wat is b ='))

if a > b :
    max = a
    min = b
    print(f'a is het grootste getal : {max}')
    print(f'Het maximum is {a}')
    print(f'Het minimum is {b}')

elif a < b :
    min = a
    max = b
    print(f'a is het kleinste getal : {min}')
    print(f'Het maximum is {b}')
    print(f'Het minimum is {a}')
else :
    print('a en b zijn even groot')





  
