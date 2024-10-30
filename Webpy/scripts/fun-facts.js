// Function to read the Word document and extract fun facts
function loadFunFactsFromDoc() {
    fetch('files/FunFacts.docx')
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
    fetch('files/FunFacts.docx')
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
