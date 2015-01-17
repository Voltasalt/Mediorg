import os
from file import MediaFile
from module import MediaModule


class MovieRenamerModule(MediaModule):
    def handle(self, media_file: MediaFile):
        import main
        name = main.settings["movie_format"].format(**media_file.metadata)

        media_file.move(os.path.join(main.settings["movie_folder"], name + media_file.extension))