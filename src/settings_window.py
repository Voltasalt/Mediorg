from PyQt5 import QtWidgets

from src import main


class SettingsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.save_callbacks = []

        self.save_button = QtWidgets.QPushButton("Save")
        self.save_button.clicked.connect(self.save)

        self.form = QtWidgets.QFormLayout()

        self.add_browse("drop_folder", "Drop folder")
        self.add_browse("tv_folder", "TV folder")
        self.add_browse("movie_folder", "Movie folder")

        self.add_string("tv_format", "TV format")
        self.add_string("movie_format", "Movie format")

        self.form.addWidget(self.save_button)

        self.setLayout(self.form)

    def browse_drop(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        if file_dialog.exec_():
            self.drop_folder_box.setText(file_dialog.selectedFiles()[0])
            
    def browse_tv(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        if file_dialog.exec_():
            self.tv_folder_box.setText(file_dialog.selectedFiles()[0])

    def add_browse(self, id, name):
        def browse():
            file_dialog = QtWidgets.QFileDialog()
            file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

            if file_dialog.exec_():
                box.setText(file_dialog.selectedFiles()[0])

        def save_callback():
            main.settings[id] = box.text()

        box = QtWidgets.QLineEdit(self)
        box.setText(main.settings[id])
        button = QtWidgets.QPushButton("...", self)
        button.clicked.connect(browse)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(box, 1)
        layout.addWidget(button, 0)

        self.form.addRow(name, layout)

        self.save_callbacks.append(save_callback)

    def add_string(self, id, name):
        def save_callback():
            main.settings[id] = box.text()

        box = QtWidgets.QLineEdit(self)
        box.setText(main.settings[id])

        self.form.addRow(name, box)

        self.save_callbacks.append(save_callback)


    def save(self):
        for cb in self.save_callbacks:
            cb()

        main.save_settings()