import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import Slider from '@mui/material/Slider';

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
    <div>
      <button onClick={handlePlay}>Play</button>
      <button onClick={handlePause}>Pause</button>
      <Slider
        value={playbackRate}
        onChange={handleSliderChange}
        min={0.1}
        max={2}
        step={0.1}
      />
    </div>
  );
}

export default ControlPanel;
