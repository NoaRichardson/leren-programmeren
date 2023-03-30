let cars = [ 
    "Audi A3",
    "BMW 3 Series",
    "Chevrolet Camaro",
    "Dodge Charger",
    "Ford Mustang",
    "Honda Civic",
    "Infiniti Q50",
    "Jaguar F-Type",
    "Kia Optima",
    "Lamborghini Huracan",
    "Mercedes-Benz C-Class",
    "Ferrari F8 Tributo",
    "Nissan Altima",
    "Porsche 911",
    "Range Rover Evoque",
    "Subaru Impreza",
    "Ferrari SF90 Stradale",
    "Tesla Model S",
    "Toyota Corolla",
    "Volkswagen Golf",
    "Acura NSX",
    "Bentley Continental",
    "Cadillac Escalade",
    "Ferrari 488 GTB",
    "Dodge Challenger",
    "Ferrari 458",
    "GMC Sierra",
    "Hyundai Elantra",
    "Jeep Grand Cherokee",
    "Ferrari SF90 Stradale",
    "Koenigsegg Agera",
    "Lexus LS",
    "Maserati GranTurismo",
    "Nissan GT-R",
    "Pagani Huayra",
    "Rolls-Royce Ghost",
    "Smart ForTwo",
    "Tesla Model X",
    "Toyota Prius",
    "Volkswagen Jetta",
    "Alfa Romeo Giulia",
    "Bugatti Chiron",
    "Chevrolet Corvette",
    "Ferrari Portofino",
    "Fiat 500",
    "GMC Yukon",
    "Honda Accord",
    "Jaguar XJ",
    "Kia Soul",
    "Lamborghini Aventador",
    "Mercedes-Benz E-Class",
    "Nissan Maxima",
    "Porsche Panamera",
    "Range Rover Sport",
    "Subaru Legacy",
    "Tesla Model 3",
    "Toyota Camry",
    "Volkswagen Passat"
    ];


// let ol = document.createElement("ol");
// new_list = cars.sort();

// for(i = 0; i < cars.length; i++){
//     let li = document.createElement("li");
//     let li_2 = document.createElement("li");
//     ol.appendChild(li);
//     li.innerHTML = li.innerHTML + new_list[i];
//     if(new_list[i].includes('Ferrari')){
//         li_2.innerHTML = li_2.innerHTML + new_list[i];
//     }
// }

cars.sort()
let ul =document.createElement('ul');
document.body.appendChild(ul);

for(x = 0; x < cars.length; x ++){
    console.log(cars[x])
    let li = document.createElement('li');
    li.innerText = cars[x];
    ul.appendChild(li);
    if(cars[x].includes('Ferrari')){
        li.classList.add('Ferrari')
    }
}

