import os
from file import MediaFile
from module import MediaModule


class TVRenamerModule(MediaModule):
    def handle(self, media_file: MediaFile):
        import main
        name = main.settings["tv_format"].format(**media_file.metadata)

        media_file.move(os.path.join(main.settings["tv_folder"], name + media_file.extension))