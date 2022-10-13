zwembad_lengte = int(input('Hoe lang is het zwembad in meters?'))
zwembad_breedte = int(input('Hoe breed is het zwembad in meters?'))
zwembad_diepte = float(input('Hoe diep is het zwembad in meters?'))

vierkante_meter = round(zwembad_lengte + zwembad_breedte, 2)
inhoud_zwembad = round(zwembad_lengte * zwembad_breedte * zwembad_diepte, 2)
kosten_uitgraven = round(inhoud_zwembad * 25.00, 2)
kosten_afvoer = round(inhoud_zwembad * 32.50, 2)
voorrijkosten = round(250 + (2.05 * 60), 2)
beton_prijs = round(200 * vierkante_meter, 2)
totaal = round(kosten_uitgraven + kosten_afvoer + voorrijkosten, 2)

print(f'Offerte voor een zwembad van {inhoud_zwembad} m3')
print(f'Uitgaven:          ${kosten_uitgraven}')
print(f'Afvoer grond       ${kosten_afvoer}')
print(f'Voorrijkosten      ${voorrijkosten}')
print(f'Beton + tegel      ${beton_prijs}')
print(f'Totaal:            ${totaal}')


