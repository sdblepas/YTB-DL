
# YouTube Video and Audio Downloader

This Python script downloads a YouTube video's highest quality video and audio streams separately and combines them into a single `.mp4` file using `ffmpeg`.

## Features

- Downloads the highest quality video and audio streams.
- Combines video and audio streams into a single `.mp4` file.
- Automatically removes temporary files after combining.
- Simple and easy to use.

## Prerequisites

### Python Packages

1. **`pytubefix`**: A fixed version of the `pytube` library to download YouTube videos. Install it via:
   ```bash
   pip install pytubefix
   ```

2. **`ffmpeg`**: Required for combining the video and audio. Ensure it is installed and added to your system's PATH. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

### System Requirements

- Python 3.6+
- A working internet connection.

## Installation

1. Clone or download this repository.
2. Ensure the required Python packages and `ffmpeg` are installed on your system.

## Usage

Run the script from the command line with a YouTube URL as an argument:

```bash
python download_video.py [YouTube URL]
```

### Example

```bash
python download_video.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Output

1. The script will create a combined video file in the current working directory with the name based on the YouTube video's title.
2. Temporary files will be cleaned up after the process completes.

### Error Handling

If you encounter any errors:
- Ensure the YouTube URL is valid.
- Check that `pytubefix` and `ffmpeg` are properly installed.
- Verify that your internet connection is stable.

## Notes

- Filenames are sanitized to remove invalid characters.
- The script overwrites the output file if it already exists.

## License

This project is licensed under the MIT License.

---

### Troubleshooting

- **Issue**: `ffmpeg` not found.
  - **Solution**: Ensure `ffmpeg` is installed and added to your system's PATH.

- **Issue**: `pytubefix` not working.
  - **Solution**: Try updating `pytubefix`:
    ```bash
    pip install --upgrade pytubefix
    ```
