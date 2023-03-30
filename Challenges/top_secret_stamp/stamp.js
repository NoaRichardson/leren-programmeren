button_clicked = 1;
var button = document.createElement("button");
button.innerHTML = "Top Secret Button";

var body = document.getElementsByTagName("body")[0];
body.appendChild(button);

button.addEventListener ("click", function() {
    document.getElementById("text").innerHTML = "Welkom Noa";
    button_clicked += 1;
    if (button_clicked > 2){
        const element = document.getElementById("text");
        element.remove();
     }
});

// let h1 = document.querySelector('h1');
//h1.innerHTML = "something";
