async function fetchData() {
    try {
        const response = await fetch('/data');
        const data = await response.json();
        // Update the UI with the received data
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}