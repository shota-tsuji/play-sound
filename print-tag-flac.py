from mutagen.flac import FLAC
import sys

args = sys.argv
filepath = args[1]
audio = FLAC(filepath)
title = audio["title"][0]
artist = audio["artist"][0]
album = audio["album"][0]

print(title)
print(artist)
print(album)
