#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout, \
    QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class Communicate(QObject):
    """
    创建一个信号，相当于事件委托
    """
    closeApp = pyqtSignal()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):

        widget = QWidget(self)
        self.setCentralWidget(widget)

        vbox = QVBoxLayout(widget)
        # 信号与槽机制
        lcd = QLCDNumber(widget)
        slide = QSlider(Qt.Horizontal, widget)
        slide.valueChanged.connect(lambda value: lcd.display(value))


        vbox.addWidget(lcd)
        vbox.addWidget(slide)

        x = 0
        y = 0
        text = "x:{0}, y:{1}".format(x, y)

        self.lable = QLabel(text, widget)
        self.setMouseTracking(True)   # 开启鼠标追踪功能
        vbox.addWidget(self.lable)

        # 事件发送者
        btn1 = QPushButton("Button 1", widget)
        btn2 = QPushButton("Button 2", widget)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.status = self.statusBar()

        # 创建事件委托
        self.c = Communicate()
        # 给事件委托绑定事件
        self.c.closeApp.connect(self.close)


        widget.setLayout(vbox)

        self.setGeometry(500, 100, 500, 500)
        self.setWindowTitle("simple")
        self.show()



    def keyPressEvent(self, event):
        """
        按键按下事件，按键按下触发
        :param event:
        :return:
        """
        if event.key() == Qt.key_Escape:
            self.close()

    def mouseMoveEvent(self, event):
        """
        鼠标移动事件
        :param event:
        :return:
        """
        x = event.x()
        y = event.y()
        text = "x:{0}, y:{1}".format(x, y)
        self.lable.setText(text)

    def buttonClicked(self):
        sender = self.sender()
        self.status.showMessage(sender.text() + "was press")

    def mousePressEvent(self, event):
        # 事件委托触发
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())