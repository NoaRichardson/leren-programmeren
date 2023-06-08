images_list = ['memory(1).jpg', 'memory(2).jpg', 'memory(3).jpg', 'memory(4).jpg', 'memory(5).jpg', 'memory(6).jpg', 'memory(7).jpg', 'memory(8).jpg', 'memory(9).jpg', 'memory(10).jpg'];
//SHUFFLE LIST
images_list = shuffle(images_list);
function shuffle(array){
    let currentIndex = array.length, randomIndex;
    while (currentIndex != 0){
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
    return array;
}
//PUTS BACKGROUND_IMAGES IN DIV
for (let i = 0; i < 20; i++){
    const div_img = document.getElementById("images")
    var images = document.createElement("img");
    images.id = i
    images.classList.add("images");
    div_img.appendChild(images);
}

function turn_image(){
    
}

for(let i = 0; i < 20; i++){
    i.onclick = turn_image();
}