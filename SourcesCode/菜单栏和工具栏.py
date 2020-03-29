#! user/bin/python3
# -*- coding: utf-8 -*-

__Author__ = "CaiTao"

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QMenu, QTextEdit
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.status = self.statusBar()  # 创建一个状态栏，该方法为QMainWindow的方法
        self.status.showMessage("Read")  # 设置状态栏信息
        textEditor = QTextEdit(self)  # 创建一个文本编辑区域

        self.setCentralWidget(textEditor)  # 设置窗口的核心部件为文本编辑区域


        menu = self.menuBar()  # 创建菜单栏
        fileMenu = menu.addMenu("&File")  # 添加一个主菜单

        # 创建一级菜单
        exitAct = QAction(QIcon(), "&Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(qApp.quit)

        # 创建一级菜单
        viewStartAct = QAction("View statusbar", self, checkable=True)  # 可勾选菜单
        viewStartAct.setStatusTip("View statusbar")
        viewStartAct.setChecked(True)  # 设置初始化勾选上
        viewStartAct.triggered.connect(self.toggleMenu)

        # 创建一级子菜单
        impMenu = QMenu("Import", self)
        # 创建二级菜单
        impAct = QAction("Import mail", self)
        impMenu.addAction(impAct)

        fileMenu.addAction(exitAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(viewStartAct)

        # 添加一个工具
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAct)

        self.setGeometry(500, 100, 400, 400)
        self.setWindowTitle("simple")
        self.show()

    def toggleMenu(self, state):
        if state:
            self.status.show()
        else:
            self.status.hide()

    def contextMenuEvent(self, event):
        """
        右键菜单事件
        """
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())