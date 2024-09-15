// Set ECMAScript version to 6 for linting (use colon instead of equals sign)
{"esversion"= 6}

// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function() {
    
    // Define the NASA API key and endpoint for Astronomy Picture of the Day (APOD)
    let apiKey = 'ZXlNkoGPeg9qsaroBYKtRv8SlyR0jnjNIY0QzBrh';
    let apiUrl = 'https://api.nasa.gov/planetary/apod?api_key=' + apiKey;

    // Fetch data from the APOD API
    fetch(apiUrl)
        .then(function(response) {
            // Check if the response is okay (status 200-299)
            if (!response.ok) {
                // Throw an error if the network response is not successful
                throw new Error('Network response was not ok');
            }
            // Convert the response to JSON format
            return response.json();
        })
        .then(function(data) {
            // Get the HTML elements where the content will be injected
            let mediaContainer = document.getElementById('apod-media-container');
            let titleElement = document.getElementById('apod-title');
            let explanationElement = document.getElementById('apod-explanation');

            // Check if all required elements exist, log an error if any are missing
            if (!mediaContainer || !titleElement || !explanationElement) {
                console.error('One or more required elements are missing.');
                return;
            }

            // Check for and remove the default APOD image if it exists (cleanup)
            let defaultApodImage = document.getElementById('default-apod-image');
            if (defaultApodImage) {
                defaultApodImage.remove();
            }

            // Display the APOD image or video based on the media type
            if (data.media_type === 'image') {
                // If the media is an image, create an img tag with the correct src and alt attributes
                mediaContainer.innerHTML = '<img src="' + data.url + '" alt="' + data.title + '" style="max-width: 100%;">';
            } else if (data.media_type === 'video') {
                // If the media is a video, create an iframe for the video embed
                mediaContainer.innerHTML = '<iframe src="' + data.url + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen style="width: 100%; height: 400px;"></iframe>';
            }

            // Update the page with the title and explanation from the APOD data
            titleElement.textContent = data.title;
            explanationElement.textContent = data.explanation;
        })
        
});
