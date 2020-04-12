from download_ui import Window
from PyQt5.QtWidgets import QApplication
import sys


class Downloader(Window):

    def __init__(self):
        super().__init__()
        self.download.connect(lambda: print("nihao"))






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Downloader()

    sys.exit(app.exec_())
