import json
import sys
import os
import time
import traceback

from PyQt5 import QtWidgets
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

from file import MediaFile
from mediatypes.movie import MovieType
import tray_icon
from mediatypes.tv import TVType


app = None
settings = {
    "drop_folder": "Drop/",
    "tv_folder": "Media/TV",
    "movie_folder": "Media/Movies",
    "tv_format": "{show}/Season {season:02}/{show} - {season}x{episode:02} - {title}",
    "movie_format": "{title} ({year}) [{quality}]"
}

types = [
    TVType(),
    MovieType()
]

class EventHandler(FileSystemEventHandler):
    def __init__(self):
        pass

    def on_any_event(self, event):
        path = event.src_path

        if isinstance(event, FileModifiedEvent):
            try:
                time.sleep(0.1)
                open(path, "a").close()
                handle(path)
            except (PermissionError, FileNotFoundError):
                pass


def load_settings():
    try:
        settings.update(json.load(open(find_appdata() + "/config.json")))
    except FileNotFoundError:
        pass


def save_settings():
    makedir(find_appdata())

    file = find_appdata() + "/config.json"

    json.dump(settings, open(file, "w"), indent=4)


def handle(path):
    file = MediaFile(path)

    for type in types:
        if type.is_applicable(file):
            try:
                for module in type.modules:
                    module.handle(file)
            except BaseException:
                traceback.print_exc()


def main():
    load_settings()
    save_settings()

    main.app = QtWidgets.QApplication(sys.argv)
    main.app.setQuitOnLastWindowClosed(False)

    trayicon = tray_icon.MediorgTray()

    event_handler = EventHandler()

    makedir(settings["drop_folder"])

    observer = Observer()
    observer.schedule(event_handler, os.path.abspath(settings["drop_folder"]), recursive=True)
    observer.start()

    sys.exit(main.app.exec_())


def makedir(dir):
    try:
        os.makedirs(os.path.abspath(dir))
    except FileExistsError:
        pass


def find_appdata():
    APPNAME = "Mediorg"
    if sys.platform == 'darwin':
        from AppKit import NSSearchPathForDirectoriesInDomains
        # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
        # NSApplicationSupportDirectory = 14
        # NSUserDomainMask = 1
        # True for expanding the tilde into a fully qualified path
        appdata = os.path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], APPNAME)
    elif sys.platform == 'win32':
        appdata = os.path.join(os.environ['APPDATA'], APPNAME)
    else:
        appdata = os.path.expanduser(os.path.join("~", "." + APPNAME))

    return appdata


if __name__ == "__main__":
    main()