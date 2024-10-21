from abc import ABC, abstractmethod

class Media_player(ABC):

    @abstractmethod
    def play(self):
        pass
class Audio_player(Media_player):

    def play(self):
        return f"Playing song.mp3"

class Video_player(Media_player):

    def play(self):
        return f"Playing video.mp4"

audio = Audio_player()
video = Video_player()
med_players = [audio, video]
for play in med_players:
    print(play.play())



# print(audio.play())
# print(video.play())