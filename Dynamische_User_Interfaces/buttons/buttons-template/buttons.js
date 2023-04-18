function click(event){
    count_1 = 0
    count_2 = 0
    count_3 = 0
    if (event.target.id == "button_1"){
        count_1 += 1;
        document.getElementById("button_1").innerHTML = count_1;
        event.target.parentElement.classList.remove("click_3");
        event.target.parentElement.classList.remove("click_2");
        event.target.parentElement.classList.add("click_1");
        document.getElementById("image_smol").style.backgroundImage = "url(images/1.jpg)";
    }else if (event.target.id == "button_2"){
        count_2 += 1;
        document.getElementById("button_2").innerHTML = count_2;
        event.target.parentElement.classList.remove("click_3");
        event.target.parentElement.classList.remove("click_1");
        event.target.parentElement.classList.add("click_2");
        event.target.parentElement.classList.add("image_2");
        document.getElementById("image_smol").style.backgroundImage = "url(images/2.jpg)";
    }else{
        count_3 += 1;
        document.getElementById("button_3").innerHTML = count_3;
        event.target.parentElement.classList.remove("click_1");
        event.target.parentElement.classList.remove("click_2");
        event.target.parentElement.classList.add("click_3");
        event.target.parentElement.classList.add("image_3");
        document.getElementById("image_smol").style.backgroundImage = "url(images/3.jpg)";
    }

}

button_1.onclick = click;
button_2.onclick = click;
button_3.onclick = click;