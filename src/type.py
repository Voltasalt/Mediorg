from file import MediaFile


class MediaType(object):
    def is_applicable(self, media_file: MediaFile) -> bool:
        return False