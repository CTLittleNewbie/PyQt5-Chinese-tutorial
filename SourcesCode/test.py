import sys
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMainWindow, QWidget


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout(self)
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)

        self.setGeometry(500, 100, 500, 500)
        self.setWindowTitle("simple")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())