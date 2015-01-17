Mediorg is a small program that sits in the background of your computer and watches a specific folder called a "Drop" folder. When you drop a media file in it (only movies and TV shows supported atm.), it will rename and organize it into your output folder.

Example:
If you drop a media file called "Family.Guy.S13E08.HDTV.x264-KILLERS.mp4" into the drop folder, it'll (with the default settings) rename it to "Family Guy - 13x08 - Our Idiot Brian.mp4" and move it to Family Guy/Season 13 in your TV output folder.
For movies, if you drop "Gone.Girl.2014.720p.BluRay.x264.YIFY.mp4", it'll get renamed to "Gone Girl (2014) [720p].mp4" in your movie output folder.

It requires Python 3, PyQt5, all the libraries in requirements.txt and a [MediaInfo](http://sourceforge.net/projects/mediainfo/files/binary/mediainfo/) CLI binary in either the program's working directory or the system PATH.

Naming formats are [plain Python format strings](https://mkaz.com/2012/10/10/python-string-format/).

Available metadata fields are:
- title (tv/movie): The title, either movie title or episode title
- year (tv/movie): The year it was aired (4-digit year)
- month (tv/movie): The month it was aired (1-12)
- day (tv/movie): The day it was aired (1-31)
- date (tv/movie): The date it was aired (ISO 8601, 1776-07-04)
- description (tv/movie): A synopsis of the movie/episode
- quality (tv/movie): The quality (480p, 720p, 1080p, etc)
- width (tv/movie): The video width in pixels
- height (tv/movie): The video height in pixels

- show (tv): The TV show title

- metascore (movie): The Metacritic score of the movie (1-100)
- imdb (movie): The IMDb ID of the movie
- rated (movie): The rating of the movie (MPAA ratings, G/PG/PG-13/R/NC-17)
- genre (movie): A list of genres
- actors (movie): A list of actors in the movie
- writers (movie): A list of writers of the movie
- director (movie): The director of the movie