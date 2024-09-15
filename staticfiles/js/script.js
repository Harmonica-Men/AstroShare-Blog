{"esversion"= 6}
document.addEventListener('DOMContentLoaded', function() {
     // Get the NASA_API_KEY passed from Django
     let apiKey = "{{ NASA_API_KEY }}";  // The API key is now passed from the backend
     let apiUrl = 'https://api.nasa.gov/planetary/apod?api_key=' + apiKey;

    fetch(apiUrl)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(function(data) {
          	let mediaContainer = document.getElementById('apod-media-container');
            let titleElement = document.getElementById('apod-title');
            let explanationElement = document.getElementById('apod-explanation');          

            // Remove default APOD image if present
            let defaultApodImage = document.getElementById('default-apod-image');
            if (defaultApodImage) {
                defaultApodImage.remove();
            }

            // Display APOD image or video
            if (data.media_type === 'image') {
                mediaContainer.innerHTML = '<img src="' + data.url + '" alt="' + data.title + '" style="max-width: 100%;">';
            } else if (data.media_type === 'video') {
                mediaContainer.innerHTML = '<iframe src="' + data.url + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen style="width: 100%; height: 400px;"></iframe>';
            }

            // Update title and explanation
            titleElement.textContent = data.title;
            explanationElement.textContent = data.explanation;
        })
        
        });