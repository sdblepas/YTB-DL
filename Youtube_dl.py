import sys
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from subprocess import run

def combine_video_audio(video_path, audio_path, output_path):
    """Combine video and audio using ffmpeg"""
    command = [
        'ffmpeg',
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        output_path,
        '-y'  # Overwrite output file if it exists
    ]
    run(command, capture_output=True)

try:
    # Check if URL was provided
    if len(sys.argv) < 2:
        print("Error: Please provide a YouTube URL as argument")
        print("Usage: python download_video.py [YouTube URL]")
        sys.exit(1)

    url = sys.argv[1]
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"\nTitle: {yt.title}")

    # Get the highest quality video stream
    video_stream = yt.streams.filter(
        adaptive=True, 
        file_extension='mp4', 
        only_video=True
    ).order_by('resolution').desc().first()

    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(
        only_audio=True, 
        file_extension='mp4'
    ).order_by('abr').desc().first()

    print("\nSelected streams:")
    print(f"Video: {video_stream.resolution}, {video_stream.filesize_mb:.1f}MB")
    print(f"Audio: {audio_stream.abr}, {audio_stream.filesize_mb:.1f}MB")

    # Create temp directory for downloads
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Download video and audio
    print("\nDownloading video...")
    video_path = video_stream.download(output_path='temp', filename='video')
    print("Downloading audio...")
    audio_path = audio_stream.download(output_path='temp', filename='audio')

    # Prepare output filename
    output_filename = f"{yt.title}_combined.mp4"
    # Remove invalid characters from filename
    output_filename = "".join(c for c in output_filename if c.isalnum() or c in (' ', '-', '_', '.')).rstrip()

    print("\nCombining video and audio...")
    combine_video_audio(video_path, audio_path, output_filename)

    # Clean up temp files
    os.remove(video_path)
    os.remove(audio_path)
    os.rmdir('temp')

    print(f"\nDownload completed! File saved as: {output_filename}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
