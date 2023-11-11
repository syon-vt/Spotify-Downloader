#imports
from youtubesearchpython import VideosSearch
from spotipy.oauth2 import SpotifyClientCredentials
from os import startfile, system
from keyboard import add_hotkey
from spotipy import Spotify
from pytube import YouTube
from os.path import isdir
from art import tprint
from time import time
from os import mkdir

#heading art
def head(): 
    tprint("Spotify    Downloader")

#spotify api credentials
client_id = ""
client_secret = ""

#misc variables
num = 0
i = 0
total_start = time()
error = 0

#initialize spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = Spotify(client_credentials_manager = client_credentials_manager)

#function to open songs folder with hotkey
import os
if isdir('Songs'):
    pass
else:
    mkdir('Songs')
def folder():
    startfile("Songs")

#hotkey to open songs folder
add_hotkey("ctrl + o", folder)

#inputs
head()
print()
link = input("Enter playlist link: ")
total_songs = int(input("Number of songs in the playlist: "))
arg = input("Enter any additional arguments(leave blank for none): ")
system('cls')
print("Press 'ctrl + O' to open the songs Folder\n")

#get playlist URI from link
uri = link.split("/")[-1].split("?")[0]


"""starts with 0 offset and takes a 100 songs then increses offset by 100 until the total number of songs is reached
this is done because the spotify api only lets you request a maximum of 100 songs at a time"""
while num<total_songs:
    try:
        for song in spotify.playlist_tracks(uri, offset=num)["items"]:

            start = time()
            name = song['track']['name']
            artist = song['track']['artists'][0]['name']
            title = f"{name} - {artist} {arg} Lyrics"
            print(title)
            videosSearch = VideosSearch(title, limit = 1)


            #searches the song name with the artist name and any extra arguments on youtube and gets the link of the video
            try:
                url = videosSearch.result().get('result')[0].get('link')
                
            except:
                try:    
                    url = videosSearch.result().get('result')[1].get('link')
                except Exception as e:
                    print(f"Failed to search {name} | {e}")
                    continue
            

            #tries to download the video with the given link

            try:
                YouTube(url).streams.filter(type='audio')[0].download(filename=f"Songs/{name} - {artist}.mp3")

                i+=1
                print(f"{i}. Downloaded {name} - {artist} ({round(time()-start, 2)}secs)\n{round((i/total_songs)*100, 2)}% Completed\n")
            except Exception as e:
                print(f"Failed to download {name} | {e}")
                error+=1

    except TypeError:
        print("Finished")
    
    num = num+100

    
#keeps console window open and displays how long the entire operation took
input(f"\n\n\nFinished in {round(time()-total_start, 2)}secs\n{error} Failed to Download...")