
let numbers = [];


while (true) {
    let num = parseFloat(prompt("Enter a number (or enter the same number to stop):"));

    if (numbers.includes(num)) {
        console.log(`The number ${num} has already been entered. Stopping the program.`);
        break;
    }

    numbers.push(num);
}

numbers.sort((a, b) => a - b);

console.log("Numbers entered in ascending order:");
numbers.forEach(number => console.log(number));

let outputDiv = document.getElementById("output");
outputDiv.innerHTML = "<h2>Numbers entered in ascending order:</h2><ul>" +
    numbers.map(number => `<li>${number}</li>`).join('') + "</ul>";