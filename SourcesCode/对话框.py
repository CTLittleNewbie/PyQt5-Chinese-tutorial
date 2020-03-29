#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QLineEdit, QInputDialog, QVBoxLayout, QHBoxLayout, QFrame, QColorDialog, \
    QLabel, QFontDialog, QSizePolicy, QFileDialog
from PyQt5.QtGui import QColor

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):

        v = QVBoxLayout()

        hbox1 = QHBoxLayout()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.showDialog)
        self.le = QLineEdit()

        hbox1.addWidget(btn)
        hbox1.addWidget(self.le)

        v.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        btn1 = QPushButton("Dialog")
        btn1.clicked.connect(self.showDialog1)
        col = QColor(0, 0, 0)

        self.fram = QFrame()
        self.fram.setMinimumSize(100, 100)
        self.fram.setMaximumSize(self.fram.minimumSize())
        self.fram.setStyleSheet("QWidget {background-color: %s}" % col.name())

        hbox2.addWidget(btn1)
        hbox2.addWidget(self.fram)
        v.addLayout(hbox2)

        hbox3 = QHBoxLayout()

        btn3 = QPushButton("Dialog")
        btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn3.clicked.connect(self.showDialog3)
        self.lbl = QLabel("Knowledge only matters")

        hbox3.addWidget(btn3)
        hbox3.addWidget(self.lbl)

        v.addLayout(hbox3)

        btn4 = QPushButton("Dialog")
        btn4.clicked.connect(self.showDialog4)
        v.addWidget(btn4)

        self.setLayout(v)

        self.setGeometry(500, 100, 500, 200)
        self.setWindowTitle("simple")
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name")
        if ok:
            self.le.setText(str(text))

    def showDialog1(self):
        col = QColorDialog.getColor()

        if col.isValid:
            self.fram.setStyleSheet("QWidget {background-color: %s}" % col.name())

    def showDialog3(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showDialog4(self):
        files = QFileDialog.getOpenFileName(self, "open file", "/PyQt5-Chinese-tutorial")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
