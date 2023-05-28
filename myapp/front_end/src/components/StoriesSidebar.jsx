// StoriesSidebar.js
import React from 'react';
import { List, ListItem, ListItemText } from '@mui/material';
import useStoriesService from '../services/StoriesService';

const StoriesSidebar = ({ onStoryClick }) => {
  const stories = useStoriesService();

  return (
    <List component="nav">
      {stories.map(story => (
        <ListItem button key={story.id} onClick={() => onStoryClick(story)}>
          <ListItemText primary={`Story ID: ${story.id}`} />
        </ListItem>
      ))}
    </List>
  );
};

export default StoriesSidebar;
