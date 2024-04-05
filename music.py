import argparse
import logging
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os
import soundfile as sf

def randomize_melody(input_file, output_file, shift_range, visualize=False):
    """
    Randomizes the melody of an audio file by shifting time frames in the spectrogram.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the output audio file.
        shift_range (int): Maximum number of frames to shift in either direction.
        visualize (bool, optional): Whether to display spectrograms before and after randomization.

    Returns:
        None
    """
    try:
        # Validate input file
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        # 1. MP3 Decomposition
        logging.info("Loading audio file: %s", input_file)
        audio_data, sample_rate = librosa.load(input_file)

        # 2. Melody Representation (Spectrogram)
        spectrogram = np.abs(librosa.stft(audio_data))

        if visualize:
            logging.info("Displaying original spectrogram")
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), y_axis='log', x_axis='time')
            plt.colorbar(format='%+2.0f dB')
            plt.title("Original Spectrogram")
            plt.show()

        # 3. Melody Randomization (Spectrogram Manipulation)
        logging.info("Randomizing spectrogram with shift range: %d", shift_range)
        randomized_spectrogram = spectrogram.copy()
        for freq_bin in range(randomized_spectrogram.shape[0]):
            randomized_spectrogram[freq_bin] = np.roll(randomized_spectrogram[freq_bin], np.random.randint(-shift_range, shift_range + 1))

        if visualize:
            logging.info("Displaying randomized spectrogram")
            plt.figure(figsize=(10, 4))
            librosa.display.specshow(librosa.amplitude_to_db(randomized_spectrogram, ref=np.max), y_axis='log', x_axis='time')
            plt.colorbar(format='%+2.0f dB')
            plt.title("Randomized Spectrogram")
            plt.show()

        # 4. Reconstruction (From Spectrogram)
        randomized_audio = librosa.istft(randomized_spectrogram * np.exp(1j * np.angle(librosa.stft(audio_data))))

        # Save the new audio file
        logging.info("Saving randomized audio to: %s", output_file)
        sf.write(output_file, randomized_audio, sample_rate)
        logging.info("Randomization complete")

    except Exception as e:
        logging.error("An error occurred: %s", str(e))

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Randomize melody of an audio file")
    parser.add_argument("input_file", help="Path to the input audio file")
    parser.add_argument("output_file", help="Path to save the output audio file")
    parser.add_argument("--shift_range", type=int, default=10, help="Maximum number of frames to shift in either direction (default: 10)")
    parser.add_argument("--visualize", action="store_true", help="Display spectrograms before and after randomization")

    args = parser.parse_args()

    randomize_melody(args.input_file, args.output_file, args.shift_range, args.visualize)