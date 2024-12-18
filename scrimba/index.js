//grab the count-el element, store it in a countEl variable
let saveEl = document.getElementById("save-el")
let resetEl = document.getElementById("reset-el")
let countEl = document.getElementById("count-el") //pass in arguments
let count = 0

console.log(saveEl)

function increment() {
    count += 1
    countEl.textContent = count
}

function save() {
    //Create a variable that contains both teh count and hte dash separator ("12 - ")
    let countStr = count + " - "
    //Render the variable in the saveEl using textContent
    saveEl.textContent += countStr
}

function reset() {
    count = 0
    countEl.textContent = 0
}