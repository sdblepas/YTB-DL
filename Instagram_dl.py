import sys
import os
import instaloader
import re
from urllib.parse import urlparse

def get_media_info(url):
    """Extract media type and identifier from Instagram URL"""
    try:
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # Handle different URL patterns
        if '/p/' in url:  # Regular post
            shortcode = re.search(r'/p/([^/]+)', url).group(1)
            return 'post', shortcode
        elif '/reels/' in url or '/reel/' in url:  # Reels
            shortcode = re.search(r'/reel(?:s)?/([^/]+)', url).group(1)
            return 'reel', shortcode
        elif '/stories/' in url:  # Stories
            username = re.search(r'/stories/([^/]+)', url).group(1)
            return 'story', username
        elif '/tv/' in url:  # IGTV
            shortcode = re.search(r'/tv/([^/]+)', url).group(1)
            return 'igtv', shortcode
        else:
            raise ValueError("Unsupported Instagram URL format")
    except (AttributeError, IndexError):
        raise ValueError(f"Could not parse URL: {url}\nPlease ensure it's a valid Instagram URL")

def download_instagram_video(url):
    """Download video from Instagram (Posts, Reels, Stories, IGTV)"""
    try:
        # Clean URL: remove query parameters and trailing slashes
        url = url.split('?')[0].rstrip('/')
        
        # Initialize Instagram loader
        L = instaloader.Instaloader(
            download_videos=True,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            compress_json=False
        )

        print("\nFetching media information...")
        
        # Get media type and identifier
        media_type, identifier = get_media_info(url)
        
        # Create temp directory
        if not os.path.exists('temp_ig'):
            os.makedirs('temp_ig')

        # Handle different types of media
        if media_type in ['post', 'reel', 'igtv']:
            post = instaloader.Post.from_shortcode(L.context, identifier)
            
            if not post.is_video:
                raise Exception("This post does not contain a video")

            print(f"\nDownloading {media_type} from @{post.owner_username}...")
            L.download_post(post, target='temp_ig')
            
            # Find and rename the downloaded video
            for file in os.listdir('temp_ig'):
                if file.endswith('.mp4'):
                    old_path = os.path.join('temp_ig', file)
                    new_filename = f"instagram_{media_type}_{identifier}.mp4"
                    os.rename(old_path, new_filename)
                    print(f"\nDownload completed! File saved as: {new_filename}")
                    break
                    
        elif media_type == 'story':
            # For stories, we need to get the profile first
            profile = instaloader.Profile.from_username(L.context, identifier)
            
            print(f"\nDownloading stories from @{profile.username}...")
            
            # Download all current stories
            L.download_stories(userids=[profile.userid], filename_target='temp_ig')
            
            # Find and rename the downloaded stories
            stories_found = False
            for file in os.listdir('temp_ig'):
                if file.endswith('.mp4'):
                    old_path = os.path.join('temp_ig', file)
                    timestamp = file.split('_')[0]  # Extract timestamp from filename
                    new_filename = f"instagram_story_{profile.username}_{timestamp}.mp4"
                    os.rename(old_path, new_filename)
                    stories_found = True
                    print(f"\nDownload completed! File saved as: {new_filename}")
            
            if not stories_found:
                raise Exception("No video stories found for this user")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Clean up temp directory
        if os.path.exists('temp_ig'):
            for file in os.listdir('temp_ig'):
                try:
                    os.remove(os.path.join('temp_ig', file))
                except Exception:
                    pass
            try:
                os.rmdir('temp_ig')
            except Exception:
                pass

if __name__ == "__main__":
    # Check if URL was provided
    if len(sys.argv) < 2:
        print("Error: Please provide an Instagram URL as argument")
        print("Usage: python Instagram_dl.py [Instagram URL]")
        print("Supported formats:")
        print("- Posts: https://www.instagram.com/p/SHORTCODE/")
        print("- Reels: https://www.instagram.com/reel/SHORTCODE/")
        print("- Stories: https://www.instagram.com/stories/USERNAME/STORYID/")
        print("- IGTV: https://www.instagram.com/tv/SHORTCODE/")
        sys.exit(1)

    url = sys.argv[1]
    download_instagram_video(url)
