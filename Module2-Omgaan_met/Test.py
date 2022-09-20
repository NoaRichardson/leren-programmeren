
dieren_dressuur = input('Heeft u pratijk ervarening met dieren-dressuur?')

if dieren_dressuur == 'ja' :

    ervaring_dieren = int(input('Hoe veel jaar ervaring heeft u?'))
    if ervaring_dieren >= 4:
       print(dieren_dressuur == 'ja')

else :
    jongleren = input('Heeft u ervaring met jongleren?')
    if jongleren == "ja":
        ervaring_jongleren = int(input('Hoe veel jaar ervaring heeft u?'))
        if ervaring_jongleren >= 5:
            print(jongleren == 'ja')
        elif ervaring_jongleren < 5:
            jongleren == 'nee'
            
    elif jongleren == 'nee':
            acrobatiek = input('Heeft u ervaring in acrobatiek?')
            if acrobatiek =='ja':
                ervaring_acrobatiek = int(input('Hoe veel jaar ervaring heeft u?'))
                if ervaring_acrobatiek >= 3:
                    print(acrobatiek == 'ja')
                elif ervaring_acrobatiek < 3:
                    ervaring = False
            elif acrobatiek == 'nee':
                ervaring = False
# eerste alle vragen stellen dan de if gebruiken
    