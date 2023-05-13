import unittest
import serial
from unittest.mock import MagicMock, patch
from src.serial_audio import setup_serial, listen_for_audio


class TestSerialAudio(unittest.TestCase):
    @patch('serial.Serial')
    def test_setup_serial(self, mock_serial):
        com_port = 'COM4'
        baud_rate = 9600
        setup_serial(com_port, baud_rate)
        mock_serial.assert_called_once_with(com_port, baud_rate)

    def test_listen_for_audio(self):
        ser = MagicMock(spec=serial.Serial)
        ser.read.side_effect = [b'\x02', b'a', b'b', b'\x03', b'\x02', b'c', b'\x03']
        gen = listen_for_audio(ser)
        self.assertEqual(next(gen), bytearray(b'ab'))
        self.assertEqual(next(gen), bytearray(b'c'))

if __name__ == '__main__':
    unittest.main()
