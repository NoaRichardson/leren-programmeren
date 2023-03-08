getal = prompt("Kies een getal");
antw = document.getElementById("antwoord");
tot = ""
tot_2 = ""

for(let y = 1; y <= getal; y ++){   
    tot += y;
    document.write(tot + "<br>")    
}

for(let i = getal; i >= 1; i --){
    for(let j = 1; j <= i; i++){
        tot_2 += j;
    }
    document.write(tot_2 + "<br>")
}
