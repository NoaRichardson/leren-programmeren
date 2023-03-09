getal = prompt("Kies een getal");
antw = document.getElementById("antwoord");
const tot = []
ruit = ""

for(let y = 1; y <= getal; y ++){   
    ruit += y + "-"
    document.write(ruit.slice(0, -1)+ "<br>");
    tot.push(ruit.slice(0,-1)+ "<br>");   
}

for(let i = getal; i >= 2; i --){
    document.write(tot[i-2]);
}
