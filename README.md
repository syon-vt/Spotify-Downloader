# Spotify-Downloader
 
A script which downloads spotify **playlists**

---
# Usage:

- Create a [Spotify App](https://developer.spotify.com/dashboard/create) and change the [`client_id`](https://github.com/syon-vt/Spotify-Downloader/blob/main/main.py#L19) and [`client_secret`](https://github.com/syon-vt/Spotify-Downloader/blob/main/main.py#L20) variables

- Run: 
```
pip install spotipy
pip install praw
pip install youtubesearchpython
pip install yt_dlp
pip install keyboard
pip install art
```

- #### Run the program and wait
---
# Issues:
- **FYI:** I created it to bypass the normal 100 songs limit on other spotify downloaders
- When tested with a 3000+ song playlist, only about 1500 got downloaded, no clue why.
- Very slow