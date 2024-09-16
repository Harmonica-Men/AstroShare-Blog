async function fetchAPOD() {
    try {
      const response = await fetch('/nasa-picture/');
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
      // Handle error silently or with an alternative approach
      // e.g., display a user-friendly message on the UI
      // document.getElementById('error-message').textContent = 'Failed to fetch data.';
    }
  }
  
  fetchAPOD();
  