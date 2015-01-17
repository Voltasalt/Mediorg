from PyQt5 import QtWidgets, QtGui

from src import settings_window


class MediorgTray(QtWidgets.QSystemTrayIcon):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.setIcon(QtGui.QIcon("assets/placeholder_icon.gif"))

        settings = settings_window.SettingsWindow()
        settings.hide()

        menu = QtWidgets.QMenu()
        menu.addAction("Settings").triggered.connect(lambda: settings.show())
        menu.addAction("Exit").triggered.connect(lambda: QtWidgets.QApplication.instance().quit())

        self.setContextMenu(menu)

        self.show()