var image = document.getElementById("image");

document.onkeydown = checkKey;
image.style.transform = "rotate(90deg)"
image.style.left = "0px"
image.style.top = "0px"
image.style.backgroundPosition = "80px 0px"

let modifier = 5;
rotateLeft = "rotate(270deg)";
rotateRight = "rotate(90deg)";
bandPosition = parseInt(image.style.backgroundPosition.replace(",", " ").split("")[0])

function checkKey(e) {
	console.log("key nr = " + e.keyCode);
    e = e || window.event;
    if(e.keyCode == 32){
    	console.log("spacebar");
    } else if (e.keyCode == '38') {  // up arrow
        console.log("Up arrow");
    } else if (e.keyCode == '40') { // down arrow
        console.log("down arrow");
    } else if (e.keyCode == '37') { // left arrow
    	console.log("left arrow");
        image.style.transform = rotateLeft;
        image.style.left = `${parseInt(image.style.left) - modifier}px`;
        bandPosition -= 84;
        image.style.backgroundPosition = bandPosition.toString() + "px " + "0px";
    } else if (e.keyCode == '39') {   // right arrow
    	console.log("right arrow");
        image.style.backgroundPosition = `164px 0px`; // check goed de rupsband (84)
        bandPosition += 84;
        image.style.transform = rotateRight;
        image.style.left = `${parseInt(image.style.left) + modifier}px`;
        image.style.backgroundPosition = bandPosition.toString() + "px " + "0px";
    }    
}