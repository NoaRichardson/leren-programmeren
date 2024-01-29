const buttonAmount = 30;

//Create buttons
for(let buttons = 1; buttons < buttonAmount + 1; buttons++){
    let button = document.createElement("button");
    button.innerHTML = buttons;
    button.classList.add(`button${buttons}`)
    const container = document.getElementById("container");
    container.appendChild(button);
    let counter = 0

    //Create event for 'click'
    button.addEventListener('click', () => {
        counter++;
        colorChange(counter, buttons)
    })
}

//Function change the color by 'click'
function colorChange(counter, buttons) {
    switch(counter) {
        case 1:
            document.getElementsByClassName(`button${buttons}`)[0].style.backgroundColor = "#FF0000";
            break;
        case 2:
            document.getElementsByClassName(`button${buttons}`)[0].style.backgroundColor = "#A020F0";
            break;
        case 3:
            document.getElementsByClassName(`button${buttons}`)[0].style.backgroundColor = "#00008B";
            break;
        case 4:
            document.getElementsByClassName(`button${buttons}`)[0].style.backgroundColor = "#000000";
            break;
        case 5:
            let button = document.getElementsByClassName(`button${buttons}`)[0];
            document.getElementById("container").removeChild(button);
            break;
    }
}