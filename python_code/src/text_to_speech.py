from elevenlabs import clone, generate, set_api_key

set_api_key("ff0f155a2fc7bec8d582e39be60bd147")

def text_to_speech(text, voice_name, output_file):
    voice = clone(
        name=voice_name,
        description="Voice description",  # Provide a suitable description for the voice
        files=[]
    )

    audio = generate(text=text, voice=voice)
    with open(output_file, "wb") as file:
        file.write(audio)
