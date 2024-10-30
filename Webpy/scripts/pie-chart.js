
// Pie chart data
const ctx = document.getElementById('myPieChart').getContext('2d');
const myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Glass', 'Metal', 'Plastic', 'Paper', 'Cardboard'],
        datasets: [{
            label: ' Distribution',
            data: [0, 0, 0, 0, 0], // Sample data values            
            backgroundColor: ['#99CCFF', '#A0A0A0', '#CCFF99', '#FFFFDC', '#FFCC99'], // Yellow shades
            borderWidth: 2,
            borderColor: 'white',
            hoverBackgroundColor: 'rgba(0,0,0,0.1)'
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
                text: 'Material Distribution',
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

// Function to fetch data from the backend and update the chart
async function updateChart() {
    try {
        const response = await fetch('http://localhost:5000/chart-data');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const newData = await response.json();
        myPieChart.data.datasets[0].data = newData;
        myPieChart.update();
    } catch (error) {
        console.error("Error updating chart data:", error.message);
    }
}
// Set an interval to fetch and update data periodically
setInterval(updateChart, 5000); // Update every 5 seconds

