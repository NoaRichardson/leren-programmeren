#input en if-statement


a = int(input('Wat is a ='))
b = int(input('Wat is b ='))

if a > b :
    Max = a
    Min = b
    print(f'a is het grootste getal : {Max}')


elif a < b :
    Min = a
    Max = b
    print(f'a is het kleinste getal : {Min}')
   
else:
    print('a en b zijn even groot')
    Min = a
    Max = b

print(f'Maximaal is a: {Max}')
print(f'Minimaal is b: {Min}')




  
