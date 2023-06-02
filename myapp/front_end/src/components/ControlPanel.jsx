import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import { Slider, IconButton, Typography, Box } from '@mui/material';
import { PlayArrow, Pause } from '@mui/icons-material';

const socket = io('http://localhost:5000'); // replace with your server address

function ControlPanel() {
  const [playbackRate, setPlaybackRate] = useState(1);

  useEffect(() => {
    // handle any events from the server here
    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from server');
    });

    socket.on('setPlaybackRate', (data) => {
      setPlaybackRate(data.playbackRate);
    });

    return () => {
      // clean up event listeners when the component is unmounted
      socket.off('connect');
      socket.off('disconnect');
      socket.off('setPlaybackRate');
    };
  }, []);

  const handlePlay = () => {
    socket.emit('play');
  };

  const handlePause = () => {
    socket.emit('pause');
  };

  const handleSliderChange = (event, newValue) => {
    setPlaybackRate(newValue);
    socket.emit('setPlaybackRate', { playbackRate: newValue });
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', m: 1 }}>
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mb: 1}}>
        <IconButton onClick={handlePlay} sx={{ mr: 2 }}>
          <PlayArrow fontSize="large" />
        </IconButton>
        <IconButton onClick={handlePause} sx={{ ml: 2 }}>
          <Pause fontSize="large" />
        </IconButton>
      </Box>
      <Typography variant="h6">Playback Speed: {playbackRate}x</Typography>
      <Slider
        value={playbackRate}
        onChange={handleSliderChange}
        min={0.1}
        max={2}
        step={0.1}
        sx={{ width: 400 }} // set the width of the slider here
      />
    </Box>
  );
}

export default ControlPanel;
