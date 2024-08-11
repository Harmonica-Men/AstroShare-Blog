document.addEventListener('DOMContentLoaded', function() {
    const apiKey = 'ZXlNkoGPeg9qsaroBYKtRv8SlyR0jnjNIY0QzBrh'; 
    const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const mediaContainer = document.getElementById('media-container');
            const imageElement = document.getElementById('image');
            const videoElement = document.getElementById('video');
            const videoSource = document.getElementById('video-source');
            const titleElement = document.getElementById('title');
            const descriptionElement = document.getElementById('description');

            // Set the title and description
            titleElement.textContent = data.title || "Astronomy Picture of the Day";
            descriptionElement.textContent = data.explanation || "No description available.";

            // Check the media type and display accordingly
            if (data.media_type === 'image') {
                imageElement.src = data.url;
                imageElement.classList.remove('d-none');
                videoElement.classList.add('d-none');
            } else if (data.media_type === 'video') {
                videoSource.src = data.url;
                videoElement.load(); // Load the video
                videoElement.classList.remove('d-none');
                imageElement.classList.add('d-none');
            } else {
                // Handle unexpected media types
                console.warn('Unexpected media type:', data.media_type);
                imageElement.classList.add('d-none');
                videoElement.classList.add('d-none');
            }
        })
        .catch(error => console.error('Error fetching the APOD data:', error));
});
