# Music-Spectrogram
 A Python tool to randomize the melody of audio files by shifting time frames in the spectrogram.
 
## Features

- Load audio files in various formats.
- Visualize the original and randomized spectrograms.
- Randomize the melody within a specified shift range.
- Save the randomized audio file.

## Requirements

- Python 3.x
- `numpy`
- `librosa`
- `matplotlib`
- `soundfile`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/melody-randomization-tool.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python randomize_melody.py input_file output_file [--shift_range SHIFT_RANGE] [--visualize]
```

- `input_file`: Path to the input audio file.
- `output_file`: Path to save the output audio file.
- `--shift_range`: Maximum number of frames to shift in either direction (default: 10).
- `--visualize`: Display spectrograms before and after randomization (optional).

## Examples

Randomize the melody of an audio file named `input.wav`:

```bash
python randomize_melody.py input.wav output.wav --shift_range 15 --visualize
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This tool was inspired by [librosa](https://librosa.org/), a Python package for music and audio analysis.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## Authors

- Amit Prakash(amit05.prakash@gmail.com)
