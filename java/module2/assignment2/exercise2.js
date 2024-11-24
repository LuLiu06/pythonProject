
let numberOfParticipants = parseInt(prompt("Enter the number of participants:"), 10);

if (isNaN(numberOfParticipants) || numberOfParticipants <= 0) {
    alert("Please enter a valid number greater than 0.");
} else {

    let participants = [];
    for (let i = 0; i < numberOfParticipants; i++) {
        let name = prompt(`Enter the name of participant ${i + 1}:`);
        participants.push(name.trim());
    }


    participants.sort();

    let participantListDiv = document.getElementById("output");
    let ol = document.createElement("ol");

    participants.forEach(name => {
        let li = document.createElement("li");
        li.textContent = name;
        ol.appendChild(li);
    });

    participantListDiv.appendChild(ol);
}
