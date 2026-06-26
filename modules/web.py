"""
import webbrowser

def handle(user_input, user_data):

    if "spotify" in user_input:
        print("Opening Spotify...")
        webbrowser.open("https://open.spotify.com")

    elif "youtube" in user_input:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "google" in user_input:
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    else:
        print("Website not recognised.")

"""

import webbrowser
import urllib.parse

def handle(user_input, user_data):


    text = user_input.lower()

    # Spotify
    if "spotify" in text:
        query = (text.replace("spotify", "")
                 .replace("play", "")
                 .replace("search", "")
                 .replace("open","")
                 .strip()
        )

        if query:
            url = "https://open.spotify.com/search/" + urllib.parse.quote(query)
        else:
            url = "https://open.spotify.com"

        print("Opening Spotify...")
        webbrowser.open(url)
        return

    # YouTube
    if "youtube" in text or "yt" in text:
        query = (text.replace("youtube", "")
                 .replace("open","")
                 .replace("search", "")
                 .replace("yt","")
                 .strip()
        )

        if query:
            url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        else:
            url = "https://www.youtube.com"

        print("Opening YouTube...")
        webbrowser.open(url)
        return

    # Wikipedia
    if "wiki" in text or "wikipedia" in text:
        query = (
            text.replace("wiki", "")
                .replace("wikipedia", "")
                .replace("search", "")
                .strip()
                .replace("open","")
        )

        if query:
            url = "https://en.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(query)
        else:
            url = "https://en.wikipedia.org"

        print("Opening Wikipedia...")
        webbrowser.open(url)
        return
    
    # Google
    if "google" in text or "what" in text:
        query = (
            text.replace("google", "")
                .replace("search", "")
                .strip()
                .replace("open","")
        )

        if query:
           url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        else:
            url = "https://google.com"

        print("Opening Google...")
        webbrowser.open(url)
        return

    # Fallback
    print("Unknown website. Searching Google...")
    url = "https://www.google.com/search?q=" + urllib.parse.quote(text)
    webbrowser.open(url)

