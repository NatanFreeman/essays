import os
import sys
import feedparser
import requests
from urllib.parse import urlparse

# Configuration
MASTODON_INSTANCE = os.environ.get("MASTODON_INSTANCE", "https://mastodon.social")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")
RSS_FEED_PATH = "public/index.xml"

def get_latest_post(feed_path):
    """Parses the RSS feed and returns the latest entry."""
    feed = feedparser.parse(feed_path)
    if not feed.entries:
        return None
    return feed.entries[0]

def get_recent_statuses(instance, token, limit=20):
    """Fetches recent statuses from the authenticated user's timeline."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{instance}/api/v1/accounts/verify_credentials"
    
    # 1. Get user ID
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Error validating token: {resp.text}")
        sys.exit(1)
    
    user_id = resp.json()["id"]
    
    # 2. Get statuses
    statuses_url = f"{instance}/api/v1/accounts/{user_id}/statuses?limit={limit}"
    resp = requests.get(statuses_url, headers=headers)
    if resp.status_code != 200:
        print(f"Error fetching statuses: {resp.text}")
        return []
        
    return resp.json()

def post_to_mastodon(instance, token, status_text, visibility="public"):
    """Posts a new status to Mastodon."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{instance}/api/v1/statuses"
    data = {
        "status": status_text,
        "visibility": visibility
    }
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 200:
        print(f"Successfully posted: {status_text}")
    else:
        print(f"Failed to post: {resp.text}")
        sys.exit(1)

def main():
    if not ACCESS_TOKEN:
        print("MASTODON_ACCESS_TOKEN not found. Skipping auto-post.")
        return

    print("Checking for new posts...")
    
    latest_post = get_latest_post(RSS_FEED_PATH)
    if not latest_post:
        print("No posts found in RSS feed.")
        return

    post_title = latest_post.title
    post_link = latest_post.link
    
    print(f"Latest post: {post_title} ({post_link})")

    # Clean up link for comparison (remove trailing slash if present)
    clean_link = post_link.rstrip("/")
    
    # Check if already posted
    recent_statuses = get_recent_statuses(MASTODON_INSTANCE, ACCESS_TOKEN)
    
    already_posted = False
    for status in recent_statuses:
        # Search in the content of the toot
        if clean_link in status["content"] or post_link in status["content"]:
            already_posted = True
            break
            
    if already_posted:
        print("Post already exists on Mastodon. Skipping.")
    else:
        print("New post detected! Publishing to Mastodon...")
        # Compose the toot
        status_text = f"{post_title}

{post_link}"
        post_to_mastodon(MASTODON_INSTANCE, ACCESS_TOKEN, status_text)

if __name__ == "__main__":
    main()
