from file import MediaFile
from module import MediaModule
from pymediainfo import MediaInfo

class MediaQualityModule(MediaModule):
    def handle(self, media_file: MediaFile):
        info = MediaInfo.parse(media_file.full_path)
        for track in info.tracks:
            if track.track_type == "Video":
                media_file.metadata["width"] = track.width
                media_file.metadata["height"] = track.height
                if track.width == 1920:
                    media_file.metadata["quality"] = "1080p"
                elif track.width == 1280:
                    media_file.metadata["quality"] = "720p"
                elif track.width == 720:
                    media_file.metadata["quality"] = "480p"
                else:
                    media_file.metadata["quality"] = str(track.height) + "p"

                break