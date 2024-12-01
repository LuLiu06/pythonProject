
const picArray = [
    {
        title: "Beautiful Sunset",
        medium_image: "https://via.placeholder.com/300x200",
        caption: "A stunning sunset over the mountains.",
        description: "Enjoy the serenity and beauty of nature with this picturesque view."
    },
    {
        title: "Ocean Waves",
        medium_image: "https://via.placeholder.com/300x200",
        caption: "Waves crashing on the beach.",
        description: "Feel the power of the ocean as waves hit the sandy shore."
    },
    {
        title: "City Lights",
        medium_image: "https://via.placeholder.com/300x200",
        caption: "The city skyline at night.",
        description: "The bustling city comes alive with twinkling lights."
    }
];


const container = document.querySelector(".container");

picArray.forEach((item) => {

    const article = document.createElement("article");
    article.classList.add("card");

    const heading = document.createElement("h2");
    heading.textContent = item.title;
    article.appendChild(heading);

    const figure = document.createElement("figure");

    const img = document.createElement("img");
    img.src = item.medium_image;
    img.alt = item.title;
    figure.appendChild(img);

    const figcaption = document.createElement("figcaption");
    figcaption.textContent = item.caption;
    figure.appendChild(figcaption);

    article.appendChild(figure);

    const paragraph = document.createElement("p");
    paragraph.textContent = item.description;
    article.appendChild(paragraph);


    container.appendChild(article);
});
