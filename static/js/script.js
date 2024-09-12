// {"esversion": 6}
document.addEventListener('DOMContentLoaded', function() {
    var apiKey = 'YOUR_NASA_API_KEY';
    var apiUrl = 'https://api.nasa.gov/planetary/apod?api_key=' + apiKey;

    fetch(apiUrl)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            var mediaContainer = document.getElementById('apod-media-container');

            if (data.media_type === 'image') {
                mediaContainer.innerHTML = '<img src="' + data.url + '" alt="' + data.title + '" style="max-width: 100%;">';
            } else if (data.media_type === 'video') {
                mediaContainer.innerHTML = '<iframe src="' + data.url + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen style="width: 100%; height: 400px;"></iframe>';
            }
            document.getElementById('apod-title').textContent = data.title;
            document.getElementById('apod-explanation').textContent = data.explanation;
        })
        .catch(function(error) {
            console.error('Error fetching APOD data:', error);
        });
});