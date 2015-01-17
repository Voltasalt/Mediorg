Mediorg is a small program that sits in the background of your computer and watches a specific folder called a "Drop" folder. When you drop a media file in it (only movies and TV shows supported atm.), it will rename and organize it into your output folder.

Example:
If you drop a media file called "Family.Guy.S13E08.HDTV.x264-KILLERS.mp4" into the drop folder, it'll (with the default settings) rename it to "Family Guy - 13x08 - Our Idiot Brian.mp4".
For movies, if you drop "Gone.Girl.2014.720p.BluRay.x264.YIFY.mp4", it'll get renamed to "Gone Girl (2014) [720p].mp4".

It requires Python, PyQt5, all the libraries in requirements.txt and a [MediaInfo](http://sourceforge.net/projects/mediainfo/files/binary/mediainfo/) CLI binary in either the program's working directory or the system PATH.
