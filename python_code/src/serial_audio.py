import serial
from scipy.io.wavfile import read, write
import io
import numpy
import requests
import os

wav_filename = 'output.wav'
path = r"C:\Users\relic\Documents\School\Engineering_Cam\Part IIA\SF4\SF4_Data_Logger\python_code\src\audio_files"

# Open serial connection, resetting Arduino
SerialData = serial.Serial('com7', 115200)

# Collecting data from serial port and convert to list of decimal integers
count = 0
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

# Convert recorded bytes into int values
CleanData = []
for i in range(len(ListData)):
    CleanData.append(int.from_bytes(ListData[i], "big"))

# Convert int values into .wav file to be used by Chat GPT API
BytesData = numpy.array(CleanData, 'uint8')

write(os.path.join(path, wav_filename), 8000, BytesData)

# Send Post Request to server
url = 'http://localhost:5000/api/audio-upload'  # replace with your server's URL
with open(os.path.join(path, wav_filename), 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)
response_data = response.json()

 
# Receive story text from Chat GPT API
Text = response_data.get('story', '')
print(Text)
# Receive story text from Chat GPT API 
# Replace with response.story_text
# Text = "Once there was a man, his name was Jim. Jim had no friends until he went to the gym and met another man called Tim."

# Send text word by word to arduino
TextList = Text.split()
print(TextList)

j = 0
while (j < 20000000): # Initial delay to ensure Arduino is ready to receive text
    j += 1


# Send text word by word to arduino
for i in range(len(TextList)):
    WordLength = len(TextList[i])
    if (WordLength > 9): #If length of string has double digits, need to indicate to arduino using ~ symbol
        SerialData.write(bytes('~' + str(WordLength - 10) + TextList[i], 'utf-8'))
    else:
        SerialData.write(bytes(str(WordLength) + TextList[i], 'utf-8'))
    
    # Further delay controls text rate, min = 1E6, max = 1E8?
    j = 0
    while (j < 5000000):
        j += 1
    
SerialData.write(bytes('#', 'utf-8')) # Send # to indicate end of text

#Close serial port resetting system
SerialData.close()
os.remove(os.path.join(path, wav_filename))
