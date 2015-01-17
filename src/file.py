import os


class MediaFile(object):
    def __init__(self, full_path: str):
        self.full_path = full_path
        self.name = os.path.basename(full_path)
        self.extension = os.path.splitext(self.name)[1]
        self.metadata = {}

    def move(self, new_path: str):
        if os.path.isdir(new_path):
            new_path = os.path.join(new_path, self.name)

        try:
            os.makedirs(os.path.dirname(new_path))

            os.rename(self.full_path, new_path)
        except FileExistsError:
            pass

        self.full_path = new_path