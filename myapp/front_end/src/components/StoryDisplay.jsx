import React from 'react';
import { Typography, Box, Card, CardMedia, CardContent, Grid } from '@mui/material';

const StoryDisplay = ({ story }) => {
  if (!story) {
    return null;
  }

  const placeholderImage = ""; // replace with your placeholder image url

  return (
    <Grid container spacing={2}>
      <Grid item xs={12} md={6}>
        <Card sx={{ m: 2, boxShadow: 3 }}>
          <CardMedia
            component="img"
            width="512"
            height="512"
            image={story.image}
            alt="Story visual representation"
          />
        </Card>
      </Grid>
      <Grid item xs={12} md={6}>
        <Card sx={{ m: 2, boxShadow: 3 }}>
          <CardContent>
            <Typography variant="h5" gutterBottom>
              {story.transcription}
            </Typography>
            <Typography variant="body1" gutterBottom>
              {story.story}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
};

export default StoryDisplay;
