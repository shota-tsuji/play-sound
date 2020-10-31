import sys
from mutagen.mp4 import MP4

args = sys.argv
filepath = args[1]
mp4 = MP4(filepath)
title = mp4.tags["\xa9nam"][0]
artist = mp4.tags["\xa9ART"][0]
album = mp4.tags["\xa9alb"][0]

print(title)
print(artist)
print(album)
