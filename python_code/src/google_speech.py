import speech_recognition as sr

def setup_recognizer():
    # Initialize recognizer instance
    return sr.Recognizer()

def transcribe_audio(recognizer, audio_file):
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # read the entire audio file

    # try to recognize speech using Google Speech Recognition
    try:
        transcript = recognizer.recognize_google(audio_data)
        print("Google Speech Recognition thinks you said " + transcript)
        return transcript
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
