// Set ECMAScript version to 6 for linting (use colon instead of equals sign)
/* {"esversion":  6} */

  // NASA API key
  // API KEY is exposed!! see Readme for explenation 'Bugs & Fixs'
  const apiKey = 'qSOjG0ja3zReYPEGfk9wFUwmv1is0lHQGjoUDvU4';

  // NASA APOD API URL
  const apiURL = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;

  // Function to fetch the APOD data
  async function fetchAPOD() {
    try {
      // Fetch the APOD data from the NASA API
      const response = await fetch(apiURL);
      const data = await response.json();

      // Select the media container and default image elements
      const apodContainer = document.getElementById('apod-media-container');
      const defaultImage = document.getElementById('default-apod-image');

      // Check if the media is an image or video
      if (data.media_type === 'image') {
        // If it's an image, update the src attribute of the default image
        defaultImage.src = data.url;
        defaultImage.alt = data.title;
      } else if (data.media_type === 'video') {
        // If it's a video, create a video iframe element
        const videoFrame = document.createElement('iframe');
        videoFrame.src = data.url;
        videoFrame.className = 'img-fluid';
        videoFrame.frameBorder = '0';
        videoFrame.allowFullscreen = true;

        // Replace the default image with the video
        apodContainer.innerHTML = '';
        apodContainer.appendChild(videoFrame);
      }
    } catch (error) {     
    // Handle error silently or with an alternative approach
    // e.g., display a user-friendly message on the UI
    // document.getElementById('error-message').textContent = 'Failed to fetch data.';
    }
  }

  // Call the function to fetch and display the APOD
  fetchAPOD();
