getal = parseInt(prompt("Kies een cijfer"));
antw = document.getElementById("antwoord");
const tot = []
ruit = ""

for(let y = 1; y <= getal; y ++){   
    x = y.toString()
    ruit += x + "-"
    document.write(ruit.slice(0, -1)+ "<br>");
    tot.push(ruit.slice(0,-1)+ "<br>");   
}

for(let i = getal; i >= 2; i--){
    document.write(tot[i-2]);
}
