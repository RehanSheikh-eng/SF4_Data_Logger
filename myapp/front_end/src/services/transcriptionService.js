export async function transcribeAudio(file) {
    // Create new FormData object and append file
    const data = new FormData();
    data.append('file', file, file.name);
  
    // Send the file to the server for transcription
    try {
      const response = await fetch('/api/transcribe', {
        method: 'POST',
        body: data,
      });
  
      // Check if the upload was successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      // Get the transcription result from the server's response
      const transcriptionResult = await response.json();
      return transcriptionResult;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  }
  