import time, vlc

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

#filename = "/home/shota/Music/MACO/MACO/メトロノーム/01-メトロノーム.mp3"
soundList = []
soundList.append("/home/shota/Music/miwa/guitarissimo/04 春になったら.m4a")
soundList.append("/home/shota/Music/かけがえなくなりたい/NO NAME-かけがえなくなりたい.flac")
#filename = "/home/shota/Music/かけがえなくなりたい/NO NAME-かけがえなくなりたい.flac"
#filename = "/home/shota/Music/かけがえなくなりたい/NO NAME-かけがえなくなりたい.flac"
for filename in soundList:
    playMusic(filename)
