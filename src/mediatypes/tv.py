from file import MediaFile
from modules.mediaquality import MediaQualityModule
from modules.thetvdb import TheTVDBModule
from modules.tvrenamer import TVRenamerModule
from type import MediaType
import re


regexes = [
    re.compile("(.*)[Ss](\d+)[Ee](\d+)"),
    re.compile("(.*)(\d+)x(\d+).*")
]

file_types = [".avi", ".mp4", ".mkv"]

class TVType(MediaType):
    def __init__(self):
        self.modules = [
            TheTVDBModule(),
            MediaQualityModule(),
            TVRenamerModule()
        ]

    def is_applicable(self, media_file: MediaFile) -> bool:
        if media_file.extension not in file_types:
            return False

        for regex in regexes:
            name = media_file.name
            name = name.replace(".", " ").replace("_", " ")

            res = regex.search(name)
            if res:
                show = res.group(1).strip()
                season = int(res.group(2).strip())
                episode = int(res.group(3).strip())

                media_file.metadata["show"] = show
                media_file.metadata["season"] = season
                media_file.metadata["episode"] = episode
                return True

        return False