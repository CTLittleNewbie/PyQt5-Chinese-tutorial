#! usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, qApp, QMessageBox,\
    QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = QFont('SansSerif', 10)  # 创建一个字体对象
        QToolTip.setFont(font)  # 给提示工具设置字体

        self.setToolTip("This is a <b>QWidget</b> widget")  # 给部件QWidget设置一个提示

        btn = QPushButton("Button", self)  # 创建一个按钮
        btn.setToolTip("This is a <b>PushButton</b> widget")  # 给按钮设置一个提示

        # 给按钮添加的三个不同的关闭窗口的事件
        # btn.clicked.connect(self.close)  # 给按钮添加点击事件
        # btn.clicked.connect(QCoreApplication.instance().quit)  # 给按钮添加点击事件
        btn.clicked.connect(qApp.quit)  # 给按钮添加点击事件

        btn.resize(btn.sizeHint())  # 设置按钮大小为默认大小
        btn.move(50, 50)  # 设置按钮位置

        self.setGeometry(250, 150, 300, 200)  # 设置窗口的几何尺寸  大小和位置
        self.setWindowTitle("Simple")  # 给窗口设置标题
        self.setWindowIcon(QIcon("../img/1.jpg"))  # 给窗口设置图表
        self.center()
        self.show()  # 显示窗口

    def center(self):
        """
        把窗口放在屏幕中间
        :return:
        """
        qr = self.frameGeometry()  # 获取窗口的框架几何
        cp = QDesktopWidget().availableGeometry().center()   # 获取屏幕中心坐标点
        qr.moveCenter(cp)  # 将窗口框架移动到屏幕中心点
        self.move(qr.topLeft())  # 将窗口移动到框架的左上角，窗口左上角为坐标原点

    def closeEvent(self, event):
        """
        重写窗口关闭事件，当窗口关闭时自动调用
        :param event:
        :return:
        """

        # 创建一个消息框
        reply = QMessageBox.question(self, "Message", "Are you sure to quit", QMessageBox.Yes | QMessageBox.No,\
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec_())
