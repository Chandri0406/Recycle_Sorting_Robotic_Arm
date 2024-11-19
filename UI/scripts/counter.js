async function fetchDataAndUpdateCounters() {
    try {
        const response = await fetch('scripts/data.json');
        const data = await response.json();

        // Check and update only if elements exist
        const glassCounter = document.querySelector('.counter-glass');
        if (glassCounter) glassCounter.textContent = `${data.glass}`;

        const metalCounter = document.querySelector('.counter-metal');
        if (metalCounter) metalCounter.textContent = `${data.metal}`;

        const plasticCounter = document.querySelector('.counter-plastic');
        if (plasticCounter) plasticCounter.textContent = `${data.plastic}`;

        const paperCounter = document.querySelector('.counter-paper');
        if (paperCounter) paperCounter.textContent = `${data.paper}`;

        const cardboardCounter = document.querySelector('.counter-cardboard');
        if (cardboardCounter) cardboardCounter.textContent = `${data.cardboard}`;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdateCounters();
    setInterval(fetchDataAndUpdateCounters, 3000); // Update every 3 seconds
});
