
function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

function main() {
    let rolls = [];
    let rollResult;

    do {
        rollResult = rollDice();
        rolls.push(rollResult);
    } while (rollResult !== 6);

    let outputDiv = document.getElementById("output");
    let listItems = rolls.map(roll => `<li>Rolled: ${roll}</li>`).join('');
    outputDiv.innerHTML = `<h2>Dice Rolls:</h2><ul>${listItems}</ul>`;
}

main();
