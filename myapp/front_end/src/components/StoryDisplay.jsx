import React from 'react';
import { Typography, Box } from '@mui/material';

const StoryDisplay = ({ story }) => {
  if (!story) {
    return null;
  }

  return (
    <Box sx={{ ml: 2 }}>
      <Typography variant="h6">Story ID: {story.id}</Typography>
      <Typography variant="body1">Story Text: {story.story}</Typography>
      <Typography variant="body1">Story Transcript: {story.transcription}</Typography>
      {story.image && <img src={story.image} alt="Story visual representation" />}
    </Box>
  );
};

export default StoryDisplay;
