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

    def transcribe(self, filename):
        preprocessed_audio = self.preprocess_audio(filename)
        with sr.AudioFile(preprocessed_audio) as source:
            audio_data = self.recognizer.record(source)
        try:
            transcript = self.recognizer.recognize_google(audio_data)
            response = jsonify({"transcription": transcript})
        except sr.UnknownValueError:
            response = jsonify({"error": "Google Speech Recognition could not understand audio"})
        except sr.RequestError as e:
            response = jsonify({"error": f"Could not request results from Google Speech Recognition service; {str(e)}"})
        finally:
            os.remove(filename) # remove the original file
            os.remove(preprocessed_audio) # remove the preprocessed file
        return response
