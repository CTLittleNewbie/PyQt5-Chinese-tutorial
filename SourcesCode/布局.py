#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit, \
    QLabel, QLineEdit


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):

        v = QVBoxLayout()

        # 盒布局
        text = QTextEdit()
        okbtn = QPushButton("OK")
        cancelbtn= QPushButton("Cancel")


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addWidget(text)
        vbox.addLayout(hbox)
        # self.setLayout(vbox)

        # 网格布局
        grid = QGridLayout()
        # self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)


        # 提交信息布局
        grid1 = QGridLayout()
        grid1.setSpacing(10)

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid1.addWidget(title, 0, 0)
        grid1.addWidget(titleEdit, 0, 1)

        grid1.addWidget(author, 1, 0)
        grid1.addWidget(authorEdit, 1, 1)

        grid1.addWidget(review, 2, 0)
        grid1.addWidget(reviewEdit, 2, 1, 5, 1)


        v.addLayout(vbox)
        v.addLayout(grid)
        v.addLayout(grid1)

        self.setLayout(v)

        self.setGeometry(500, 100, 400, 500)
        self.setWindowTitle("simple")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())