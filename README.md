
# YTB-DL

YTB-DL is a Python-based command-line tool for downloading videos from YouTube and other video platforms. It allows you to download videos in the highest quality or extract audio as needed, with support for combining video and audio using FFmpeg.

## Features

- Download videos in the highest available quality.
- Extract and download audio from videos.
- Combine video and audio streams into a single file using FFmpeg.
- Batch downloading support for playlists.
- Simple and easy-to-use CLI interface.

## Prerequisites

Before using YTB-DL, ensure you have the following installed:

1. **Python 3.6+**:
   - YTB-DL is built using Python and requires version 3.6 or higher.
2. **FFmpeg**:
   - Used for processing video and audio. Install it from [FFmpeg's official website](https://ffmpeg.org/download.html) and ensure it is added to your system's PATH.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sdblepas/YTB-DL.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YTB-DL
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with a YouTube URL:

```bash
python ytb_dl.py [OPTIONS] URL
```

### Options

- `-f, --format` : Specify the video format (e.g., `best`, `mp4`, `webm`).
- `-o, --output` : Define the output directory.
- `-a, --audio-only` : Download only the audio stream.
- `-p, --playlist` : Download all videos in a playlist.

### Examples

1. **Download the highest quality video**:

   ```bash
   python ytb_dl.py -f best https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

2. **Download audio only**:

   ```bash
   python ytb_dl.py -a https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

3. **Download an entire playlist**:

   ```bash
   python ytb_dl.py -p https://www.youtube.com/playlist?list=PL1234567890abcdef
   ```

## Output

The downloaded files will be saved in the specified output directory or the current directory if no output is specified. Temporary files used during processing will be automatically cleaned up.

## Troubleshooting

1. **`ffmpeg` not found**:
   - Ensure `ffmpeg` is installed and added to your system's PATH.

2. **`pytube` errors**:
   - Update the `pytube` library:
     ```bash
     pip install --upgrade pytube
     ```

## Contributing

Contributions are welcome! If you'd like to improve this project, fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Downloading videos from YouTube or other platforms may violate their terms of service. Ensure you have the necessary permissions before downloading any content.

---

Happy downloading!
