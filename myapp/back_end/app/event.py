from flask import request
from flask_socketio import emit
from .extensions import socketio

@socketio.on('connect')
def test_connect():
    print("Client Connected")

@socketio.on('disconnect')
def test_disconnect():
    print('Client Disconnected')

@socketio.on('play')
def handle_play():
    # Handle play command
    print("Play was clicked")
    emit('play', broadcast=True)

@socketio.on('pause')
def handle_pause():
    # Handle pause command
    print("Pause was clicked")
    emit('pause', broadcast=True)

@socketio.on('setPlaybackRate')
def handle_set_playback_rate(data):
    playback_rate = data['playbackRate']
    print('Set playback rate to', playback_rate)
    # Do something with playback_rate here...
    emit('setPlaybackRate', {'playbackRate': playback_rate}, broadcast=True)
