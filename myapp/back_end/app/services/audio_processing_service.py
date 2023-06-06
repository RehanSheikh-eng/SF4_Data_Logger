import numpy as np
from scipy.signal import wiener
import torch
import torchaudio
from denoiser import pretrained
from denoiser.dsp import convert_audio

class AudioProcessingService:
    def __init__(self):
        # Load the Facebook model
        self.model = pretrained.dns64().cuda()

    def process_audio(self, audio_file_path, method='fb'):
        """
        Process audio_file using specified method.

        audio_file_path: Path to the audio file to be processed.
        method: The processing method. Either 'wiener' or 'fb'. Defaults to 'fb'.
        """
        try:
            # Load the noisy wav file
            wav, sr = torchaudio.load(audio_file_path)
            wav = convert_audio(wav.cuda(), sr, self.model.sample_rate, self.model.chin)

            if method == 'wiener':
                # Convert the data back to a numpy array for the Wiener filter
                wav_np = wav.data.cpu().numpy()

                # Apply the Wiener filter to the original data
                denoised_wiener = wiener(wav_np)

                return denoised_wiener

            elif method == 'fb':
                # Apply the Facebook model to the data
                with torch.no_grad():
                    denoised_fb = self.model(wav[None])[0]

                # Convert the denoised data back to a numpy array
                denoised_fb_np = denoised_fb.data.cpu().numpy()

                return denoised_fb_np

            else:
                raise ValueError("Invalid processing method. Choose either 'wiener' or 'fb'.")
                
        except Exception as e:
            raise e
