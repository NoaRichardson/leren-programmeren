prijs_iphone = int(input('Hoe duur is de iPhone?'))
prijs_samsung = int(input('Hoe duur is de Samsung?'))
prijs_zenfone = int(input('Hoe duur is de Zenfone?'))

if prijs_iphone > prijs_samsung:
    duurst = prijs_iphone
    goedkoopst = prijs_samsung
    duurst_telefoon = 'iPhone'
    goedkoopst_telefoon = 'samsung'

elif prijs_iphone < prijs_samsung:
    duurst = prijs_samsung
    goedkoopst = prijs_iphone
    duurst_telefoon = 'samsung'
    goedkoopst_telefoon = 'iPhone'   
 
if (prijs_iphone >= 900) and (prijs_samsung >= 900):
    print(f'De {duurst_telefoon} is het duurst, de telefoon kost : {duurst}')
    print(f'De {goedkoopst_telefoon} is het goedkoopst, de telefoon kost : {goedkoopst}')
    print('Het advies is dus geen telefoon te kopen, ze zijn te duur')

elif prijs_iphone == prijs_samsung:
    print('De iphone en samsung zijn even duur')

elif prijs_iphone < prijs_samsung or prijs_iphone > prijs_samsung:
    verschil = duurst - goedkoopst    
    print(f'De {duurst_telefoon} is het duurst, de telefoon kost : {duurst}')
    print(f'De {goedkoopst_telefoon} is het goedkoopst, de telefoon kost : {goedkoopst}')
    print(f'Het advies is dus de {goedkoopst_telefoon} te kopen. Deze is namelijk {verschil} euro goedkoper dan de {duurst_telefoon}')
    
