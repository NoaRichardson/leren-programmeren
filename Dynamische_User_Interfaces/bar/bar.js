menu = ['wijn', 'fris', 'bier']
let prijs_wijn = 4.50
let prijs_fris = 2.00
let prijs_bier = 2.25
let tot_wijn = 0
let tot_fris = 0
let tot_bier = 0
let th_wijn = 0
let th_fris = 0
let th_bier = 0

function bestelling(drank){
    drank = prompt("Wat wil je?")
    return drank
}

function in_menu(drank){
    test = menu.includes(drank);
    if (Boolean(test)){
        return drank
    }else{
        alert("Dat hebben we niet");
        return drank
    }
}

function hoeveel_drank(drank){
    hoeveel = parseInt(prompt("Hoeveel?"))
    if (drank === 'wijn'){
        duur_wijn = hoeveel * prijs_wijn
        th_wijn = th_wijn + hoeveel
        tot_wijn += duur_wijn
        return duur_wijn, th_wijn, tot_wijn
    }else if(drank === 'fris'){
        duur_fris = hoeveel * prijs_fris
        th_fris = th_fris + hoeveel
        tot_fris += duur_fris
        return duur_fris, th_fris, tot_fris
    }else{
        duur_bier = hoeveel * prijs_bier
        th_bier = th_bier + hoeveel
        tot_bier += duur_bier
        return duur_bier, th_bier, tot_bier
    }
}

function bon(hoeveel){
    totaal = tot_wijn + tot_fris + tot_bier
    if(tot_wijn > 0){
        document.write("Wijn" + " " + th_wijn + "x" + " " + tot_wijn + "<br>")
    }if(tot_fris > 0){
        document.write("Fris" + " " + th_fris + "x" + " " + tot_fris + "<br>")
    }if (tot_bier > 0){
        document.write("Bier" + " " + th_bier + "x" + " " + tot_bier + "<br>")
    }
    document.write("Totaal" + " " + totaal)
}


drank = ""
while (drank != 'stop'){
    drank = bestelling(drank)
    if (drank != 'stop'){
        test = menu.includes(drank)
        if(Boolean(test)){
            hoeveel = hoeveel_drank(drank)
        }else{
            alert("Dat hebben we niet")
            drank = bestelling(drank)
        }
    }
    }
bon(hoeveel)