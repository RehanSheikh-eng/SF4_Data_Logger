import os
import speech_recognition as sr
from pydub import AudioSegment
from flask import jsonify

class TranscriptionService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def preprocess_audio(self, audio_file):
        audio = AudioSegment.from_file(audio_file)
        audio = audio.set_frame_rate(16000)
        audio = audio.apply_gain(-20 - audio.dBFS)
        preprocessed_audio_file = 'preprocessed_' + audio_file
        audio.export(preprocessed_audio_file, format='wav')
        return preprocessed_audio_file

    def transcribe(self, filename, preprocess_audio=False):
        if preprocess_audio:
            filename = self.preprocess_audio(filename)
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

