from flask_socketio import SocketIO

def register(socketio):
    @socketio.on('play')
    def handle_play():
        # Handle play command
        socketio.emit('play', broadcast=True)

    @socketio.on('pause')
    def handle_pause():
        # Handle pause command
        socketio.emit('pause', broadcast=True)
