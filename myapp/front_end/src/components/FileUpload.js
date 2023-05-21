import React, { useState } from 'react';
import { transcribeAudio } from '../services/transcriptionService';
import TranscriptionDisplay from './TranscriptionDisplay';
function FileUpload() {
  const [file, setFile] = useState(null);
  const [transcript, setTranscript] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUploadClick = async () => {
    if (!file) {
      return;
    }

    const transcriptionResult = await transcribeAudio(file);
    setTranscript(transcriptionResult.transcription);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUploadClick}>Transcribe</button>
      {transcript && <TranscriptionDisplay transcript={transcript} />}
    </div>
  );
}

export default FileUpload;
