const buttonVotes = [
    {'id': 0, "name" : "partij1", "votes" : 0},
    {'id': 1, "name" : "partij2", "votes" : 0},
    {'id': 2, "name" : "partij3", "votes" : 0},
    {'id': 3, "name" : "partij4", "votes" : 0}
]

//Create buttons through loop
buttonVotes.forEach((item) => {
    //Create the buttons
    let button = document.createElement("button");
    button.innerHTML = item.name;
    let contentContainer = document.getElementById("vote");
    contentContainer.appendChild(button);
    
    //Create event for the buttons
    button.onclick = function() {
        addVote(item.id);
    }
})

//Create result button
const resultButton = document.createElement("button");
resultButton.innerHTML = "Stemmen tellen";
resultButton.classList.add("result_button")
const contentContainer = document.getElementById("vote");
contentContainer.appendChild(resultButton);

//Create event for result button
resultButton.onclick = function() {
    countUp();
}

//-----FUNCTION-----//

//Function for buttons
function addVote(id){
 buttonVotes.find(item => item.id === id).votes++;
}

//Function for result button
function countUp(){
    //Remove all buttons
    while (contentContainer.firstChild) {
        contentContainer.removeChild(contentContainer.firstChild);
    }
    //Create result title
    let resultTitle = document.createElement("h1");
    resultTitle.innerHTML = "Uitslag van het aantal stemmen:";
    contentContainer.appendChild(resultTitle);

    //Create the results of voting
    buttonVotes.forEach((item) => {
        let results = document.createElement("p");
        results.innerHTML = `${item["votes"]} stemmen voor ${item["name"]}`;
        contentContainer.appendChild(results);
    })
    
    //Calc party with the most votes
    let mostVoted = document.createElement('h2');
    let listVotes = buttonVotes.map(({votes}) => votes);
    let highestValue = Math.max.apply(Math, listVotes);
    let test  = buttonVotes.filter(({ votes }) => votes === highestValue);
    let highestNames = [];
    test.forEach((item) => {
        highestNames.push(item["name"]);
    })
    mostVoted.innerHTML = `Partij met meeste stemmen: ${highestNames}`;
    contentContainer.appendChild(mostVoted);
    contentContainer.style.flexDirection = "column";
}