import re
from file import MediaFile
from modules.mediaquality import MediaQualityModule
from modules.movierenamer import MovieRenamerModule
from modules.omdb import OMDbModule
from type import MediaType


regexes = [
    re.compile("(.*)((19|20)\d{2})"),
]

file_types = [".avi", ".mp4", ".mkv"]

class MovieType(MediaType):
    def __init__(self):
        self.modules = [
            OMDbModule(),
            MediaQualityModule(),
            MovieRenamerModule()
        ]

    def is_applicable(self, media_file: MediaFile):
        if media_file.extension not in file_types:
            return False

        for regex in regexes:
            name = media_file.name
            name = name.replace(".", " ").replace("_", " ")

            res = regex.search(name)
            if res:
                title = res.group(1).strip()
                year = int(res.group(2).strip())

                media_file.metadata["title"] = title
                media_file.metadata["year"] = year
                return True

        return False