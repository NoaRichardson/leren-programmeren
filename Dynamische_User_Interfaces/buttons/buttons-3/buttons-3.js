buttonAmount = 30;

//Create buttons
for(let buttons = 1; buttons < buttonAmount + 1; buttons++){
    let button = document.createElement("button");
    button.innerHTML = buttons;
    button.classList.add("button")
    const container = document.getElementById("container");
    container.appendChild(button);
    let counter = 0

    //Create event for 'click'
    button.addEventListener('click', () => {
        counter++;
        colorChange(counter)
    })
}

//Function change the color by 'click'
function colorChange(counter) {
    switch(counter) {
        case 1:
            document.getElementsByClassName("button").style.backgroundColor = "#FF0000";//--Try array with objects keeping the counter by to solve
    }
}