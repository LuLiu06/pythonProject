
function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

function main() {

    let sides = parseInt(prompt("Enter the number of sides on the dice:"));


    if (isNaN(sides) || sides <= 0) {
        alert("Please enter a valid number of sides (greater than 0).");
        return;
    }

    let rolls = [];
    let rollResult;


    do {
        rollResult = rollDice(sides);
        rolls.push(rollResult);
    } while (rollResult !== sides);

    let outputDiv = document.getElementById("output");
    let listItems = rolls.map(roll => `<li>Rolled: ${roll}</li>`).join('');
    outputDiv.innerHTML = `<h2>Dice Rolls (Maximum is ${sides}):</h2><ul>${listItems}</ul>`;
}

main();
