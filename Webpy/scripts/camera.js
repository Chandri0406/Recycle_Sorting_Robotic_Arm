// toggleView.js

function toggleView() {
    const chartSection = document.getElementById("chart-section");
    const cameraSection = document.getElementById("camera-section");

    chartSection.classList.toggle("hidden");
    cameraSection.classList.toggle("hidden");
}

function startCameraAndOpenPage() {
    const video = document.getElementById("camera-feed");

    // Prompt for permission to access the camera
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
            video.play();
        })
        .catch((error) => {
            console.error("Camera access denied:", error);
        });
}

function stopCamera() {
    const video = document.getElementById("camera-feed");
    const stream = video.srcObject;
    if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach((track) => track.stop());
        video.srcObject = null;
    }
}
