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

function bestelling(){
    order = prompt("Wat wil je?")
    if(order === "stop"){
        bon()
    }else{
        in_menu()
    }
}

function in_menu(){
    test = menu.includes(order);
    if (Boolean(test)){
        hoeveel_drank()
    }else{
        alert("Dat hebben we niet");
        bestelling()
    }
}

function hoeveel_drank(){
    hoeveel = parseInt(prompt("Hoeveel?"))
    if (order === 'wijn'){
        duur_wijn = hoeveel * prijs_wijn
        th_wijn = th_wijn + hoeveel
        tot_wijn += duur_wijn
        bestelling()
    }else if(order === 'fris'){
        duur_fris = hoeveel * prijs_fris
        th_fris = th_fris + hoeveel
        tot_fris += duur_fris
        bestelling()
    }else{
        duur_bier = hoeveel * prijs_bier
        th_bier = th_bier + hoeveel
        tot_bier += duur_bier
        bestelling()
    }
}

function bon(){
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

bestelling()

drank = ""
while (drank != 'stop'){
    drank = vraag_drank()
    if (drank != 'stop'){
        bestelling = verwerk_bestelling(drank) 
    }
}
print_bon(bestelling)