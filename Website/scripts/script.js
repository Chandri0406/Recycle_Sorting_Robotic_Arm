
// Pie chart data
const ctx = document.getElementById('myPieChart').getContext('2d');
const myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Recyclable', 'Compostable', 'Trash'],
        datasets: [{
            label: 'Waste Material Distribution',
            data: [50, 30, 20], // Sample data values            
            backgroundColor: ['rgb(64, 82, 116)', 'rgb(97, 197, 135)', 'rgb(234, 211, 83)'], // Yellow shades
            borderWidth: 2,
            borderColor: 'white',
            hoverBackgroundColor: 'rgba(64, 82, 116, 0.8)'
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
                labels: {
                    font: {
                        size: 14,
                        style: 'italic'
                    },
                    color: 'antiquewhite',
                    boxWidth: 15
                }
            },
            title: {
                display: true,
                text: 'Waste Material Distribution',
                color: 'antiquewhite',
                font: {
                    size: 20,
                    weight: 'bold'
                },
                padding: {
                    top: 10,
                    bottom: 30
                }
            },
            tooltip: {
                backgroundColor: 'rgba(0,0,0,0.7)',
                cornerRadius: 8,
                bodyFont: {
                    size: 14
                },
                titleFont: {
                    size: 16,
                    weight: 'bold'
                }
            },
            animation: {
                duration: 2500,    // Animation duration in milliseconds
                easing: 'easeOutElastic',  // Animation easing function (e.g., 'linear', 'easeInQuad', etc.)
            },

        }
    }
});

// Set width and height in JavaScript
document.getElementById('myPieChart').width = 400;
document.getElementById('myPieChart').height = 400;

// Function to read the Word document and extract fun facts
function loadFunFactsFromDoc() {
    fetch('FunFacts.docx')
        .then(response => response.arrayBuffer())
        .then(data => {
            mammoth.extractRawText({ arrayBuffer: data })
                .then(result => {
                    const funFactsText = result.value; // Get the plain text from the document
                    const funFactsArray = funFactsText.split('\n').filter(fact => fact.trim() !== ''); // Split into lines and remove empty ones

                    // Update fun facts array with the loaded fun facts
                    funFacts.length = 0; // Clear existing fun facts
                    funFacts.push(...funFactsArray); // Add new fun facts

                    // Display the first fun fact
                    updateFunFact();
                })
                .catch(err => console.log("Error reading document:", err));
        })
        .catch(err => console.log("Error fetching document:", err));
}

// Function to select a random recycling fun fact
function getRandomFunFact() {
    const randomIndex = Math.floor(Math.random() * funFacts.length);
    return funFacts[randomIndex];
}

// Function to update the fun fact on the page
function updateFunFact() {
    const factElement = document.querySelector('.facts ul');
    factElement.innerHTML = `<li>${getRandomFunFact()}</li>`;
}

// Initial call to load the fun facts from the Word document
loadFunFactsFromDoc();

// Set interval to update fun fact every 20 seconds (20,000 milliseconds)
setInterval(updateFunFact, 20000);

// Array to hold the fun facts
let funFacts = [];

// Function to read the Word document and extract fun facts
function loadFunFactsFromDoc() {
    fetch('FunFacts.docx')
        .then(response => response.arrayBuffer())
        .then(data => {
            // Use Mammoth to extract text from the Word document
            mammoth.extractRawText({ arrayBuffer: data })
                .then(result => {
                    const funFactsText = result.value; // Get the plain text from the document
                    funFacts = funFactsText.split('\n').filter(fact => fact.trim() !== ''); // Split by line and remove empty entries

                    // Start displaying the first fun fact
                    updateFunFact();
                })
                .catch(err => console.error("Error reading document:", err));
        })
        .catch(err => console.error("Error fetching document:", err));
}

// Function to select a random recycling fun fact
function getRandomFunFact() {
    const randomIndex = Math.floor(Math.random() * funFacts.length);
    return funFacts[randomIndex];
}

// Function to update the fun fact on the page
function updateFunFact() {
    const factElement = document.querySelector('.facts ul');
    const newFact = getRandomFunFact();
    factElement.innerHTML = `<li>${newFact}</li>`;
}

// Initial call to load the fun facts from the Word document
loadFunFactsFromDoc();

// Set interval to update the fun fact every 20 seconds (20,000 milliseconds)
setInterval(updateFunFact, 20000);
