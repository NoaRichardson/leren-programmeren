getal = prompt("Kies een getal");
antw = document.getElementById("antwoord");
tot = ""
tot_2 = " "

for(i = 1; i <= getal; i ++){   
    tot += i;
    document.write(tot + "<br>")    
}

for(let i = 1; i < getal - 1; i --){
    for(let j = 1; j < i; i ++){
        tot_2 += j;
    }
    document.write(tot_2 + "<br>")
}
