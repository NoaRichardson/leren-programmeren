#Sollicitatie.py 

name = input('Wat is je naam?')
leeftijd = input('Hoe oud ben je?')

print(f'Welcome {name} dit is een test om te kijken of je geschikt bent voor deze baan veel succes')

gender = input('Bent u een man of vrouw?')

if gender == 'man':
   gender_ = 1

elif gender == 'vrouw':
     gender_ = 2

if gender_ == 1:
   snor = input('Heeft u een snor?')
   if snor == 'ja':
       snor_lengte = int(input('Hoe lang is u snor in cm?'))
       if snor_lengte >= 10:
         print(gender == 'man')
         man_met_goede_snor = True
            
elif gender_ == 2:
   haar_kleur = input('Wat is u haar kleur?')
   if haar_kleur == 'rood':
      haar_style = input('Heeft u stel of krullend haar?')
      if haar_style == 'krullend':
         haar_lengte = int(input('Hoe lang is u haar in cm?'))
         if haar_lengte >= 20:
            print(gender == 'vrouw')
            vrouw_met_juist_haar = True

      
lengte = int(input('Hoe lang bent u in cm?'))
if lengte >= 150:
      print(lengte)
      lengte = True
   
wegen = int(input('Hoe veel weegt u in kg?'))
if wegen >= 90:
      print(wegen)
      wegen = True
      
hoge_hoed = input('heeft u een hoge hoed?')
if hoge_hoed == 'ja':
   print(hoge_hoed)
   hoge_hoed = True

opleiding = input('Is u in bezit van een Diploma MBO-4 ondernemen?')
if opleiding == 'ja':
   print(opleiding)
   opleiding = True 

rijbewijs = input('Is u in bezit van een geldig Vrachtwagen rijbewijs?')
if rijbewijs == 'ja':
   print(rijbewijs)
   rijbewijs = True
      
certificaat = input('Heeft u een Certificaat “Overleven met gevaarlijk personeel?')
if certificaat == 'ja':
   print(certificaat)
   certificaat = True


ervaring = input('Heeft u ervaring in dieren-dressuur, jongleren of acrobatiek zo ja welke?')
if ervaring == 'dieren-dressuur':
   hoelang = int(input('Hoe veel jaar?'))
   if hoelang >= 4:
      print(ervaring)
      ervaring = True

if ervaring == 'jongleren':
   hoelang_jongleren = int(input('Hoe veel jaar?'))
   if hoelang_jongleren >= 5:
      print(ervaring)
      ervaring = True
   
if ervaring == 'acrobatiek':
   hoelang_acrobatiek = int(input('Hoe veel jaar?'))
   if hoelang_acrobatiek >= 3:
      print(ervaring)
      ervaring = True

if (man_met_goede_snor or vrouw_met_juist_haar) and lengte and wegen and hoge_hoed and opleiding and rijbewijs and certificaat and ervaring:
   print('U bent aangenomen')
else:
   print('U bent niet aangenomen')