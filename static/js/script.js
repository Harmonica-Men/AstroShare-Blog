async function fetchAPOD() {
  try {
      const response = await fetch('/apod/');
      const data = await response.json();

      const apodContainer = document.getElementById('apod-media-container');
      const defaultImage = document.getElementById('default-apod-image');

      if (data.media_type === 'image') {
          defaultImage.src = data.url;
          defaultImage.alt = data.title;
      } else if (data.media_type === 'video') {
          const videoFrame = document.createElement('iframe');
          videoFrame.src = data.url;
          videoFrame.className = 'img-fluid';
          videoFrame.frameBorder = '0';
          videoFrame.allowFullscreen = true;

          apodContainer.innerHTML = '';
          apodContainer.appendChild(videoFrame);
      }
  } catch (error) {
      console.error('Error fetching APOD:', error);
  }
}

fetchAPOD();
