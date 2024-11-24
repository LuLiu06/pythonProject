
let dogs = [];
for (let i = 0; i < 6; i++) {
    let dogName = prompt(`Enter the name of dog ${i + 1}:`);
    dogs.push(dogName.trim());
}

dogs.sort().reverse();

let dogListDiv = document.getElementById("output");
let ul = document.createElement("ul");

dogs.forEach(name => {
    let li = document.createElement("li");
    li.textContent = name;
    ul.appendChild(li);
});

dogListDiv.appendChild(ul);
