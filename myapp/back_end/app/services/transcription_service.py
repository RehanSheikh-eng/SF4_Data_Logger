import os
import speech_recognition as sr
from pydub import AudioSegment
from flask import jsonify

class TranscriptionService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, filename):
        with sr.AudioFile(filename) as source:
            audio_data = self.recognizer.record(source)
        transcript = ""
        try:
            transcript = self.recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {str(e)}")
        return transcript

