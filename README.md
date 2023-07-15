# SF4 Data Logger

This project logs audio data from an Arduino device and processes it in Python.

## Project Structure

- `arduino_code/` - Contains Arduino sketches for interfacing with peripherals like microphone, LCD, speaker etc.
- `python_code/` 
  - `src/` - Python source code
    - `client.py` - Sends audio data to backend API
    - `serial_audio.py` - Handles serial communication with Arduino
    - `text_to_speech.py` - Text-to-speech conversion
  - `test/` - Test scripts
- `doc/` - Documentation files like README  
- `myapp/` - Backend Flask API
  - `back_end/` - Backend code
  - `front_end/` - Frontend / UI code
- `.gitignore` - Git ignore file
- `main.py` - Main Python script  

## Setup

### Hardware

- Arduino Uno
- Microphone
- Speaker 
- LCD display
- Breadboard
- Wires
- Computer with mic and speaker

### Software

- Arduino IDE
- Python 3.7+
- Flask 
- PySerial 
- gTTS

### Installation

1. Clone the repo
   ```
   git clone https://github.com/<username>/<repo>.git
   ```
2. Install Python dependencies
   ```
   pip install -r requirements.txt 
   ```
3. Install Arduino IDE and required libraries

## Usage

1. Flash the Arduino sketch `arduino_code/Arduino_interface/Arduino_interface.ino`
2. Run the Flask API:
   ```
   cd myapp/back_end
   python run.py
   ```  
3. Run the main Python script:
   ```
   python main.py
   ```
4. Speak into the microphone connected to the Arduino
5. Audio will be sent to the API and processed

## Configuration

- The Arduino COM port can be configured in `serial_audio.py`
- API endpoints are defined in `myapp/back_end/routes/`
- API keys and credentials should be specified in the `.env` file

## Testing

Unit tests for core modules are under `python_code/tests/`. Run them with:

```
python -m unittest discover -s test
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub.
