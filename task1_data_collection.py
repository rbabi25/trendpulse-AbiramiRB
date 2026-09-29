"""
TrendPulse - Task 1: Fetch, Categorize, and Save HackerNews Trending Stories
"""

import os
import time
import json
from datetime import datetime

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
NEW_STORIES_URL = "https://hacker-news.firebaseio.com/v0/newstories.json"
ITEM_URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HEADERS = {"User-Agent": "TrendPulse/1.0"}

NUM_IDS_TO_FETCH = 500        # how many IDs to pull from EACH endpoint (top + new)
STORIES_PER_CATEGORY = 25     # cap per category
REQUEST_TIMEOUT = 10          # seconds, per HTTP request
SLEEP_BETWEEN_CATEGORIES = 2  # seconds, once per category loop (not per story)

# Category -> keywords (matched case-insensitively against the story title)
CATEGORY_KEYWORDS = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_story_id_list(url, limit=NUM_IDS_TO_FETCH):
    """Fetch a list of story IDs from a given HackerNews endpoint. Returns a list of ints."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        story_ids = response.json()
        return story_ids[:limit]
    except requests.RequestException as e:
        print(f"Failed to fetch story IDs from {url}: {e}")
        return []


def fetch_all_candidate_ids():
    """
    Combine top stories + new stories into one deduplicated pool.
    Rarer categories (sports, science) need a bigger pool to find 25 matches,
    since HackerNews's "top" list alone skews heavily toward tech content.
    """
    top_ids = fetch_story_id_list(TOP_STORIES_URL)
    new_ids = fetch_story_id_list(NEW_STORIES_URL)

    # dict.fromkeys() removes duplicates while preserving order
    # (a plain set() would work too, but would scramble the order)
    combined = list(dict.fromkeys(top_ids + new_ids))
    print(f"Combined pool: {len(top_ids)} top + {len(new_ids)} new = {len(combined)} unique IDs")
    return combined


def fetch_story_details(story_id):
    """Fetch a single story's details. Returns a dict, or None if the request fails."""
    url = ITEM_URL_TEMPLATE.format(story_id)
    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None


def match_category(title, keywords):
    """Return True if the title contains any of the keywords (case-insensitive)."""
    if not title:
        return False
    title_lower = title.lower()
    return any(keyword.lower() in title_lower for keyword in keywords)


def build_story_record(raw_story, category):
    """Pull out the 7 required fields from a raw HackerNews story dict."""
    return {
        "post_id": raw_story.get("id"),
        "title": raw_story.get("title"),
        "category": category,
        "score": raw_story.get("score"),
        "num_comments": raw_story.get("descendants", 0),
        "author": raw_story.get("by"),
        "collected_at": datetime.now().isoformat(),
    }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def collect_stories():
    """
    Fetch story IDs once, then loop over each category, scanning through
    stories to find matches until that category's quota is filled.
    """
    story_ids = fetch_all_candidate_ids()
    if not story_ids:
        print("No story IDs fetched — aborting.")
        return []

    # Cache fetched story details so we don't re-fetch the same story
    # multiple times across category loops.
    story_cache = {}

    all_collected = []

    for category, keywords in CATEGORY_KEYWORDS.items():
        print(f"\nCollecting category: {category}")
        category_stories = []

        for story_id in story_ids:
            if len(category_stories) >= STORIES_PER_CATEGORY:
                break  # quota filled for this category

            # Use cached details if we already fetched this story for
            # an earlier category; otherwise fetch it now.
            if story_id in story_cache:
                raw_story = story_cache[story_id]
            else:
                raw_story = fetch_story_details(story_id)
                story_cache[story_id] = raw_story

            if raw_story is None:
                continue  # failed fetch, already printed a message, move on

            title = raw_story.get("title", "")
            if match_category(title, keywords):
                record = build_story_record(raw_story, category)
                category_stories.append(record)

        print(f"  -> Found {len(category_stories)} stories for '{category}'")
        all_collected.extend(category_stories)

        # One sleep per category loop, not per individual story fetch.
        time.sleep(SLEEP_BETWEEN_CATEGORIES)

    return all_collected


def save_stories(stories):
    """Save the collected stories to data/trends_YYYYMMDD.json."""
    os.makedirs("data", exist_ok=True)
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2)

    print(f"\nCollected {len(stories)} stories. Saved to {filename}")
    return filename


def main():
    stories = collect_stories()
    save_stories(stories)


if __name__ == "__main__":
    main()
