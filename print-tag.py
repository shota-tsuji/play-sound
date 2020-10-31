from mutagen.easyid3 import EasyID3
import sys

args = sys.argv
#path = "/home/shota/Music/MACO/MACO/メトロノーム/01-メトロノーム.mp3"
path = args[1]
tags = EasyID3(path)
print(EasyID3.valid_keys.keys())
#print(tags.pprint())
print(tags['title'][0])
print(tags['artist'][0])
print(tags['album'][0])
print(tags['tracknumber'][0])
#print(tags['discnumber'])
