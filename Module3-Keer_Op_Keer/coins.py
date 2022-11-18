# Noa Richardson: 
# 99072699:
# purpose of program: 
# function of program:
# structure of program: 
coin_500 = 0
coin_200 = 0
coin_100 = 0
coin_50 = 0
coin_20 = 0
coin_10 = 0
coin_5 = 0
coin_2 = 0
coin_1 = 0



toPay = int(float(input('Amount to pay: '))* 100) # input Wat je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # input Wat er is betaald
change = paid - toPay # Hoeveel te veel is betaald

if change > 0: #Als de change moet krijgen word de coinValue 50 cent
  coinValue = 50 # coinValue word 50
  
  while change > 0 or coinValue > 0: # Als je change moet krijgen start de while loop
    nrCoins = change // coinValue # floor division
    nrCoinsReturned = 0

    if nrCoins > 0: # Als de nrCoins groter is dan 0 run hij dit
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Laat zien hoeveel coins van hoeveel cent je moet terug geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # input wat je terug geeft
      change -= nrCoinsReturned * coinValue # Haalt het van de change af en word het nieuwe getal van change

# comment on code below: Als je niet alles in 50 cent kan terug betalen laat het zien hoe je van coins van minder cent hoeveel je daar voor moet betalen
    if coinValue == 500:
       coin_500 = nrCoinsReturned
       coinValue = 200
    elif coinValue == 200:
      coin_200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      coin_100 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      coin_50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      coin_20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      coin_10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      coin_5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      coin_2 =nrCoinsReturned
      coinValue = 1
    else:
      coinValue = 0
      coin_1 = nrCoinsReturned

if change > 0: # Als de change groter is dan 0 print hij dit
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  print('Returned:')
  print(f"5 euro {coin_500}")
  print(f"2 euro {coin_200}")
  print(f"1 euro {coin_100}")
  print(f"50 cent {coin_50}")
  print(f"20 cent {coin_20}")
  print(f"10 cent {coin_10}")
  print(f"5 cent {coin_5}")
  print(f"2 cent {coin_2}")
  print(f"1 cent {coin_1}")
