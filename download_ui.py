from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
import sys
import os


class Window(QWidget):
    download = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        tab_widget = QTabWidget(self)
        tab_widget.setGeometry(0, 0, 400, 300)
        tab1 = QWidget(tab_widget)
        tab2 = QWidget(tab_widget)
        tab_widget.addTab(tab1, "single download")
        tab_widget.addTab(tab2, "list download")

        vertical = QVBoxLayout(tab1)

        horizontal1 = QHBoxLayout(tab1)
        url_name = QLabel("URL:", tab1)
        url_value = QLineEdit(tab1)
        horizontal1.addWidget(url_name)
        horizontal1.addWidget(url_value)

        horizontal2 = QHBoxLayout(tab1)
        path_name = QLabel("URL:", tab1)
        path_value = QLineEdit(tab1)
        path_btn = QPushButton(tab1)
        path_btn.setIcon(QIcon("images/timg.jpg"))
        path_btn.clicked.connect(lambda: self.open_directory(path_value))
        horizontal2.addWidget(path_name)
        horizontal2.addWidget(path_value)
        horizontal2.addWidget(path_btn)

        text = QTextEdit(tab1)

        horizontal3 = QHBoxLayout(tab1)
        enter = QPushButton("下载", tab1)
        enter.clicked.connect(self.download.emit)
        horizontal3.addStretch(1)
        horizontal3.addWidget(enter)

        vertical.addLayout(horizontal1)
        vertical.addLayout(horizontal2)
        vertical.addWidget(text)
        vertical.addStretch(1)
        vertical.addLayout(horizontal3)


        self.setWindowTitle("download")
        self.setGeometry(500, 500, 400, 300)
        self.show()

    def open_directory(self, path_value):
        file = QFileDialog.getExistingDirectory(self, "select directory", os.curdir)
        if file:
            path_value.setText(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec_())
