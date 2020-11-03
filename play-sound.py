# goal: プレイリストデータベースの作成(ファイルパスとしてではなく，曲として列挙する目的であればOK)

import time, vlc
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
import sys

def printInfo(filename):
    ext = filename.split(".")
    print(ext)
    if(ext[-1] == "mp3"):
        tags = EasyID3(filename)
        title = tags['title'][0]
        artist = tags['artist'][0]
        album = tags['album'][0]
        print("title:", title)
        print(artist)
        print(album)
    elif(ext[-1] == "m4a"):
        mp4 = MP4(filename)
        title = mp4.tags["\xa9nam"][0]
        artist = mp4.tags["\xa9ART"][0]
        album = mp4.tags["\xa9alb"][0]
        print("title:", title)
        print(artist)
        print(album)
    elif(ext[-1] == "flac"):
        audio = FLAC(filename)
        title = audio["title"][0]
        artist = audio["artist"][0]
        album = audio["album"][0]
        print("title:", title)
        print(artist)
        print(album)

def playMusic(source):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(source)
    player.set_media(media)

    player.play()
    time.sleep(1.5)
    durationSec = player.get_length() / 1000.0
    time.sleep(durationSec)
    print("Duration: " + str(durationSec) + " [sec]")

args = sys.argv
playlistfile = open(args[1], 'r')
songs = playlistfile.readlines()
#filename = args[1]
for song in songs:
    print(song.strip())
    printInfo(song.strip())
    playMusic(song.strip())
