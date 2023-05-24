function click(event){
    var nummer = this.id.replace("button_", "")
    this.count++
    this.innerHTML = this.count;
    container.className =""
    event.target.parentElement.classList.add("click_" + nummer);
    document.getElementById("image_smol").style.backgroundImage = "url(images/"+ nummer + ".jpg)";
    button_list = document.querySelectorAll("button")
    for(let button of button_list){
        button.disabled = false;
    }
    this.disabled = true;

}

button_1.onclick = click;
button_1.count = 0;
button_2.onclick = click;
button_2.count = 0;
button_3.onclick = click;
button_3.count = 0;

// replace, this, ++, query, button of buttonlist