let numbers = [];
while (true) {
    let num = parseFloat(prompt("Enter a number (enter 0 to stop):"));
    if (num === 0) break;
    numbers.push(num);
}


numbers.sort((a, b) => b - a);


console.log("Numbers from largest to smallest:");
numbers.forEach(number => console.log(number));

let outputDiv=document.getElementById("output")
outputDiv.innerHTML="<ul>" +numbers.map(number=>`<li>${number}</li>`).join('') + "</ul>";