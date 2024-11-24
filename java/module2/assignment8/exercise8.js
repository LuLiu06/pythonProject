
function concat(strings) {
    let result = "";

    for (let i = 0; i < strings.length; i++) {
        result += strings[i];
    }
    return result;
}
let names = ["Johnny", "DeeDee", "Joey", "Marky"];
let concatenatedString = concat(names);

document.getElementById("output").innerHTML = `<p>The concatenated string is: ${concatenatedString}</p>`;
