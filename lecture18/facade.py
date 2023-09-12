
class AudioSystem:
    def open_audio(self, file):
        print(f"Opening audio file: {file}")

    def play_audio(self):
        print("Playing audio")


class VideoSystem:
    def open_video(self, file):
        print(f"Opening video file: {file}")

    def play_video(self):
        print("Playing video")


class MultimediaFacade:
    def __init__(self):
        self.audio = AudioSystem()
        self.video = VideoSystem()

    def play_audio(self, file):
        self.audio.open_audio(file)
        self.audio.play_audio()

    def play_video(self, file):
        self.video.open_video(file)
        self.video.play_video()


multimedia = MultimediaFacade()

multimedia.play_audio("music.mp3")

multimedia.play_video("movie.mp4")
