import unittest
from src.google_speech import *
import speech_recognition as sr
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")


class TestGoogleSpeech(unittest.TestCase):
    def setUp(self):
        self.recognizer = setup_recognizer()

    def test_setup_recognizer(self):
        self.assertIsInstance(self.recognizer, sr.Recognizer)

    def test_transcribe_audio(self):
        transcript = transcribe_audio(self.recognizer, AUDIO_FILE)  # replace with path to an actual wav file
        print(transcript)
        self.assertIsInstance(transcript, str)
        self.assertEqual(transcript, "1 2 3")

if __name__ == "__main__":
    unittest.main()
