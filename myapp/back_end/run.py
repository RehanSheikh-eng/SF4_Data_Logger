from app import create_app, socketio
from flask_cors import CORS


app = create_app()
CORS(app, origins="*")


if __name__ == '__main__':
    #app.run(debug=True, port=5000)
    socketio.run(app, port=5000)


