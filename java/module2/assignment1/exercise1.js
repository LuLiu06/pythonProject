let numbers = [];
for (let i = 0; i < 5; i++) {
    let num = parseFloat(prompt(`Enter number ${i + 1}:`));
    numbers.push(num);
}


let outputDiv = document.getElementById('output');
outputDiv.innerHTML = "<h2>Numbers in reverse order:</h2>";

for (let i = numbers.length - 1; i >= 0; i--) {
    outputDiv.innerHTML += `<p>${numbers[i]}</p>`;
}