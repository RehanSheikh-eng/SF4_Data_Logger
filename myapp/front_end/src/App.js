// App.js
import React, { useState } from 'react';
import { Divider, Box } from '@mui/material';
import StoriesSidebar from './components/StoriesSidebar';
import StoryDisplay from './components/StoryDisplay';
import ControlPanel from './components/ControlPanel';

const App = () => {
  const [selectedStory, setSelectedStory] = useState(null);

  const handleStoryClick = (story) => {
    setSelectedStory(story);
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'row', p: 1 }}>
      <StoriesSidebar onStoryClick={handleStoryClick} />
      <Divider orientation="vertical" flexItem />
      <StoryDisplay story={selectedStory} />
      <ControlPanel></ControlPanel>
    </Box>
  );
};

export default App;
