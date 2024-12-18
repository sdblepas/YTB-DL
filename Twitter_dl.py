import sys
import os
from tweety_ns import Twitter

def download_twitter_video(url):
    """Download video from Twitter"""
    try:
        # Initialize Twitter client (no authentication needed for public tweets)
        app = Twitter()

        print("\nFetching tweet information...")
        # Extract tweet ID from URL
        tweet_id = url.split('/')[-1].split('?')[0]
        
        # Get tweet details
        tweet = app.tweet_detail(tweet_id)
        
        if not tweet.media:
            raise Exception("No media found in this tweet")

        # Find video in tweet media
        video = None
        for media in tweet.media:
            if media.type == 'video':
                video = media
                break

        if not video:
            raise Exception("No video found in this tweet")

        # Get the highest quality video variant
        video_url = max(video.variants, key=lambda x: x.bitrate if hasattr(x, 'bitrate') else 0).url
        
        # Prepare output filename
        output_filename = f"twitter_video_{tweet_id}.mp4"
        
        print(f"\nDownloading video from tweet by @{tweet.author.username}...")
        
        # Download the video
        app.download_media(video_url, output_filename)
        
        print(f"\nDownload completed! File saved as: {output_filename}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Check if URL was provided
    if len(sys.argv) < 2:
        print("Error: Please provide a Twitter video URL as argument")
        print("Usage: python Twitter_dl.py [Twitter URL]")
        sys.exit(1)

    url = sys.argv[1]
    download_twitter_video(url)
