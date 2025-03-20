# Audio Player

## Overview
This is a simple command-line audio player built using Python and Pygame. The application allows users to list and select audio files from a specified directory and provides basic playback controls such as play, pause, unpause, and stop.

## Features
- List available MP3 files in the `audio` directory.
- Play a selected audio file.
- Pause and unpause playback.
- Stop playback.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Clone or download the repository.
2. Install the required dependency using pip:
   ```sh
   pip install pygame
   ```
3. Create an `audio` directory in the project folder and add your `.mp3` files.

## Usage
Run the script using:
```sh
python audio_player.py
```

### Controls:
- Select an audio file by entering its corresponding number.
- Enter:
  - `1` to pause
  - `2` to unpause
  - `3` to stop and exit
  - `4` to exit immediately

## Notes
- Ensure that the `audio` directory exists and contains MP3 files.
- The script only supports `.mp3` files.

## Disclaimer
This project is designed for general audio playback purposes. I am not responsible for how users utilize this software, including listening to music that may go against their personal beliefs.

## License
This project is open-source and free to use.

