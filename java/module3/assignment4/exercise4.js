
const students = [
    { value: "2345768", name: "John" },
    { value: "2134657", name: "Paul" },
    { value: "5423679", name: "Jones" }
];

const targetElement = document.getElementById("target");

students.forEach((student) => {
    const option = document.createElement("option");

    option.value = student.value;
    option.textContent = student.name;

    targetElement.appendChild(option);
});
