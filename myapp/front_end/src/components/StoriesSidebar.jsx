import React from 'react';
import { List, ListItem, ListItemText, Button } from '@mui/material';
import useStoriesService from '../services/StoriesService';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles({
  listItem: {
    marginBottom: '10px',
    border: '1px solid #ddd',
    borderRadius: '5px',
    '&:hover': {
      backgroundColor: '#f5f5f5',
    },
  },
  list: {
    maxHeight: '80vh',
    overflowY: 'auto',
    '&::-webkit-scrollbar': {
      width: '0.5em',
    },
    '&::-webkit-scrollbar-thumb': {
      backgroundColor: 'slategrey',
      // outline: '1px solid slategrey'
    }
  },
  button: {
    marginTop: '10px',
  },
});

const StoriesSidebar = ({ onStoryClick }) => {
  const classes = useStyles();
  const stories = useStoriesService();

  return (
    
    <div>
      <Button variant="contained" color="primary" className={classes.button}>
        Add Story
      </Button>
      <List component="nav" className={classes.list}>
        {stories.map(story => (
          <ListItem button key={story.id} onClick={() => onStoryClick(story)} className={classes.listItem}>
            <ListItemText primary={`${story.transcription}`} />
          </ListItem>
        ))}
      </List>

    </div>
  );
};

export default StoriesSidebar;
