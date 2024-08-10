document.addEventListener('DOMContentLoaded', function() {
    const apiKey = 'ZXlNkoGPeg9qsaroBYKtRv8SlyR0jnjNIY0QzBrh'; // Replace with your NASA API key
    const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            document.getElementById('title').textContent = data.title;
            document.getElementById('image').src = data.url;
            document.getElementById('description').textContent = data.explanation;
            
        })
        .catch(error => console.error('Error fetching the APOD data:', error));
});
