prijs_spel = 24.95
korting = 0.4

aantal = int(input('Hoeveel games koop je?'))
inkoop_prijs = (prijs_spel - prijs_spel * korting) * aantal
totaal = ((aantal - 1) * 0.25) + 1 + inkoop_prijs

print(inkoop_prijs)
print(totaal)
