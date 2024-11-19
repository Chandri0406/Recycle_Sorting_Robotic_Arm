
async function fetchDataAndUpdateChart() {
    try {
        const response = await fetch('scripts/data.json');
        const data = await response.json();

        const ctx = document.getElementById('myChart');
        if (!ctx) {
            console.error("Canvas element with id 'myChart' not found.");
            return;
        }

        // Use fetched data values instead of undefined variables
        const chartData = [data.glass, data.metal, data.plastic, data.paper, data.cardboard];

        if (window.myPieChart && window.myPieChart.data && window.myPieChart.data.datasets) {
            // Update existing chart data
            window.myPieChart.data.datasets[0].data = chartData;
            window.myPieChart.update();
        } else {
            // Initialize chart if not already done
            myPieChart = new Chart(ctx.getContext('2d'), {
            type: 'pie',
            data: {
                labels: ['Glass', 'Metal', 'Plastic', 'Paper', 'Cardboard'],
                datasets: [{
                    label: ' Distribution',
                    data: chartData,// Sample data values            
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
    }
} catch (error) {
    console.error('Error fetching data:', error);
}
}

// Set width and height in JavaScript
document.getElementById('myChart').width = 400;
document.getElementById('myChart').height = 400;

// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdateChart();
    setInterval(fetchDataAndUpdateChart, 3000); // Update every 3 seconds
});