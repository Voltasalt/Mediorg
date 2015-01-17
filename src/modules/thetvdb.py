from file import MediaFile
from module import MediaModule

import tvdb_api

class TheTVDBModule(MediaModule):
    def __init__(self):
        self.t = tvdb_api.Tvdb()

    def handle(self, media_file: MediaFile):
        s = self.t[media_file.metadata["show"]]
        sd = s.data
        e = s[media_file.metadata["season"]][media_file.metadata["episode"]]

        m = media_file.metadata
        m["date"] = e["firstaired"]
        m["year"] = int(e["firstaired"].split("-")[0])
        m["month"] = int(e["firstaired"].split("-")[1])
        m["day"] = int(e["firstaired"].split("-")[2])
        m["title"] = e["episodename"]
        m["language"] = e["language"]
        m["description"] = e["overview"]
        m["show"] = sd["seriesname"]