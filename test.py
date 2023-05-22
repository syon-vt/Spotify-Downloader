from yt_dlp import YoutubeDL
from time import time
from moviepy.editor import VideoFileClip

start = time()
ydl_opts = {
    'outtmpl': f'test/%(title)s.%(ext)s',
    "quiet": True

}
url = "https://www.youtube.com/watch?v=g5vSnczfxo8&ab_channel=Bassn"
vid = VideoFileClip(YoutubeDL(ydl_opts).download(url))
vid.audio.write_audiofile(r"my_result.mp3")
print(round(time()-start, 2))
