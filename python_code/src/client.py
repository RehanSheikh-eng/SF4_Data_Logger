import socketio
import serial
from scipy.io.wavfile import read, write
import numpy
import requests
import os
import time


sio = socketio.Client()
wav_filename = 'output.wav'
path = r"C:\Users\relic\Documents\School\Engineering_Cam\Part IIA\SF4\SF4_Data_Logger\python_code\src\audio_files"
url = 'http://localhost:5000/api/audio-upload'  # replace with your server's URL


is_playing = True  # If the system is currently playing or paused
playback_rate = 1.0  # The rate at which the text is being sent to the Arduino

# Open serial connection, resetting Arduino
SerialData = serial.Serial('com7', 115200)
# Test mode
test_mode = False


@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('play')
def handle_play():
    global is_playing
    print("Play event received")
    is_playing = True

@sio.on('pause')
def handle_pause():
    global is_playing
    print("Pause event received")
   is_playing = False

@sio.on('setPlaybackRate')
def handle_set_playback_rate(data):
    global playback_rate
    playback_rate = data['playbackRate']
    print('Set playback rate to', playback_rate)

def read_serial_data():
    ListData = []
    while True: # Wait for 0 byte from Arduino - indicating start of recording
        if (SerialData.read() == b'\x00'):
            break

    while True: # Add recorded bytes to array until 0 byte received - indicating end of recording
        Data = SerialData.read()
        if (Data != b'\x00'):
            ListData.append(Data)
        else:
            break
    return ListData

def make_api_call():
    with open(os.path.join(path, wav_filename), 'rb') as f:
        files = {'file': f}
        try:
            response = requests.post(url, files=files)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with the API request: {e}")
            return None
    return response.json()

def send_text_to_arduino(Text):
    TextList = Text.split()
    print(TextList)
    i = 0
    while i < len(TextList):
        if not is_playing:
            time.sleep(0.1)  # Sleep for a short while if not playing
            continue
        SerialData.write(bytes(str(len(TextList[i])) + TextList[i], 'utf-8')) # Length of each word sent before word
        time.sleep(1.0 / playback_rate)  # Sleep for some time based on the playback rate
        i += 1
    SerialData.write(b'\xCF') # Send 0 byte to indicate end of text

sio.connect('http://localhost:5000', wait_timeout = 10)

while True:  # Adding the infinite loop here
    # Collecting data from serial port and convert to list of decimal integers
    ListData = read_serial_data()

    # Convert recorded bytes into int values
    CleanData = [int.from_bytes(data, "big") for data in ListData]

    # Convert int values into .wav file to be used by Chat GPT API
    BytesData = numpy.array(CleanData, 'uint8')
    write(os.path.join(path, wav_filename), 8000, BytesData)

    # Send Post req to server

    if not test_mode:
        response_data = make_api_call()

        # Receive story text from Chat GPT API
        if response_data is not None:
            Text = response_data.get('story', '')
            print(Text)
    else:
        Text = "This is a test response. No API call was made."

    # Send text word by word to Arduino
    send_text_to_arduino(Text)

    # Close serial port resetting system
    SerialData.close()
    os.remove(os.path.join(path, wav_filename))