// App.js
import React, { useState } from 'react';
import { Grid } from '@mui/material';
import StoriesSidebar from './components/StoriesSidebar';
import StoryDisplay from './components/StoryDisplay';
import ControlPanel from './components/ControlPanel';

const App = () => {
  const [selectedStory, setSelectedStory] = useState(null);

  const handleStoryClick = (story) => {
    setSelectedStory(story);
  };

  return (
    <Grid container>
      <Grid item xs={3}>
        <StoriesSidebar onStoryClick={handleStoryClick} />
      </Grid>
      <Grid item xs={9}>
        <StoryDisplay story={selectedStory} />
      </Grid>
      <Grid item xs={12}>
        <ControlPanel />
      </Grid>
    </Grid>
  );
};

export default App;
