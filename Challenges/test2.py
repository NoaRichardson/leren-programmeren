print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 

leeftijd = int(input('Hoe oud ben je?'))
pasje = input('Heb je een pasje?')
begeleider = input('Heb je een begeleider?')
if begeleider == 'ja':
  naam_begeleider = input('Wat is de naam van je begeleider?')
  leeftijd_begeleider = int(input("Hoe oud is je begeleider?"))
else:
  naam_begeleider = 0
  leeftijd_begeleider = 0

if leeftijd <= 12 and begeleider == 'ja' and leeftijd_begeleider >= 20 or leeftijd < 14 and pasje == 'ja' or leeftijd <= 12 and naam_begeleider == 'Vladimir':
  print('Je bent welcome')
else:
  print('Je bent niet welcome')