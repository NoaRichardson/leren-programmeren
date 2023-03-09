let giraffen_aantal = prompt("Hoeveel giraffen zijn er?");
let struisvogels_aantal = prompt("Hoeveel struisvogel zijn er?");
let zebra_aantal = prompt("Hoeveel Zebra's zijn er?");

function aantal_poten(giraffen_aantal, struisvogels_aantal, zebra_aantal) {
    giraffen = giraffen_aantal * 4
    struisvogels = struisvogels_aantal * 2
    zebras = zebra_aantal * 4
    poten = giraffen + struisvogels + zebras
    return poten
}
document.write(aantal_poten(giraffen_aantal, struisvogels_aantal, zebra_aantal))
