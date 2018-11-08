from flask import Flask
from flask_socketio import SocketIO, send, emit
from PIL import Image
import io
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('speech_to_text')
def handleImageProcessing(audio):
