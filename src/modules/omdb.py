import datetime

import requests

from file import MediaFile
from module import MediaModule


class OMDbModule(MediaModule):
    def handle(self, media_file: MediaFile):
        params = {
            "s": media_file.metadata["title"],
            "type": "movie",
            "v": "1"
        }

        if "year" in media_file.metadata:
            params["y"] = media_file.metadata["year"]

        sr = requests.get("http://www.omdbapi.com/", params=params)
        id = sr.json()["Search"][0]["imdbID"]

        dr = requests.get("http://www.omdbapi.com/", params={
            "i": id
        }).json()

        date = datetime.datetime.strptime(dr["Released"], "%d %b %Y").date()

        m = media_file.metadata
        if "Title" in dr:
            m["title"] = dr["Title"]
        if "Year" in dr:
            m["year"] = int(dr["Year"])
        m["month"] = date.month
        m["day"] = date.day
        m["date"] = date.strftime("%Y-%m-%d")
        m["imdb"] = id
        if "Metascore" in dr:
            m["metascore"] = dr["Metascore"]
        if "Plot" in dr:
            m["description"] = dr["Plot"]
        if "Rated" in dr:
            m["rated"] = dr["Rated"]
        if "Genre" in dr:
            m["genres"] = dr["Genre"].split(", ")
        if "Actors" in dr:
            m["actors"] = dr["Actors"].split(", ")
        if "Writers" in dr:
            m["writers"] = dr["Writers"].split(", ")
        if "Director" in dr:
            m["director"] = dr["Director"]