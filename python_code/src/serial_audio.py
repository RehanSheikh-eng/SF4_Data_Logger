import serial

def setup_serial(com_port, baud_rate=9600):
    return serial.Serial(com_port, baud_rate)

def listen_for_audio(ser):
    audio_data = bytearray()

    while True:
        data = ser.read()
        if data[0] == 0x02:  # start byte
            audio_data.clear()
        elif data[0] == 0x03:  # end byte
            yield audio_data
            audio_data.clear()
        else:
            audio_data.append(data[0])
