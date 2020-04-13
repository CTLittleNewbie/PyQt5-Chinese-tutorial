# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 320)
        Form.setMinimumSize(QtCore.QSize(400, 320))
        Form.setMaximumSize(QtCore.QSize(400, 320))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"    background-image: url(:/newPrefix/Images/bg.png) ;\n"
"    \n"
"}")
        self.main_menu_btn = QtWidgets.QPushButton(Form)
        self.main_menu_btn.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.main_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background-color:rgb(237, 161, 255);\n"
"    border:2px solid rgb(255, 128, 200);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{    \n"
"    border:4px solid rgb(255, 61, 246);    \n"
"}\n"
"QPushButton:checked{    \n"
"    background-color:rgb(255, 24, 124);;    \n"
"}")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.about_menu_btn = QtWidgets.QPushButton(Form)
        self.about_menu_btn.setGeometry(QtCore.QRect(100, 20, 40, 40))
        self.about_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background-color:rgb(237, 161, 255);\n"
"    border:2px solid rgb(255, 128, 200);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{    \n"
"    border:4px solid rgb(255, 61, 246);    \n"
"}\n"
"QPushButton:checked{    \n"
"    background-color:rgb(255, 24, 124);;    \n"
"}")
        self.about_menu_btn.setObjectName("about_menu_btn")
        self.exit_menu_btn = QtWidgets.QPushButton(Form)
        self.exit_menu_btn.setGeometry(QtCore.QRect(20, 100, 40, 40))
        self.exit_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background-color:rgb(237, 161, 255);\n"
"    border:2px solid rgb(255, 128, 200);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{    \n"
"    border:4px solid rgb(255, 61, 246);    \n"
"}\n"
"QPushButton:checked{    \n"
"    background-color:rgb(255, 24, 124);;    \n"
"}")
        self.exit_menu_btn.setObjectName("exit_menu_btn")
        self.reset_menu_btn = QtWidgets.QPushButton(Form)
        self.reset_menu_btn.setGeometry(QtCore.QRect(77, 77, 40, 40))
        self.reset_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background-color:rgb(237, 161, 255);\n"
"    border:2px solid rgb(255, 128, 200);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{    \n"
"    border:4px solid rgb(255, 61, 246);    \n"
"}\n"
"QPushButton:checked{    \n"
"    background-color:rgb(255, 24, 124);;    \n"
"}")
        self.reset_menu_btn.setObjectName("reset_menu_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 150, 201, 150))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color:rgb(98, 116, 90);    \n"
"    font: 10pt \"MV Boli\";\n"
"}")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background:transparent;    \n"
"    border-bottom:1px solid rgb(101, 111, 104);\n"
"    border-style:outset;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:rgb(98, 116, 90);    \n"
"    font: 10pt \"MV Boli\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background:transparent;    \n"
"    border-bottom:1px solid rgb(101, 111, 104);\n"
"    border-style:outset;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:rgb(98, 116, 90);    \n"
"    font: 10pt \"MV Boli\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background:transparent;    \n"
"    border-bottom:1px solid rgb(101, 111, 104);\n"
"    border-style:outset;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.register_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 195, 98);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 123, 220);    \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(97, 24, 255);    \n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
        self.about_menu_btn.raise_()
        self.exit_menu_btn.raise_()
        self.reset_menu_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menu_btn.raise_()

        self.retranslateUi(Form)
        self.main_menu_btn.clicked['bool'].connect(Form.show_hide_menu)
        self.about_menu_btn.clicked.connect(Form.about_lk)
        self.exit_menu_btn.clicked.connect(Form.exit_panel)
        self.reset_menu_btn.clicked.connect(Form.reset)
        self.register_btn.clicked.connect(Form.check_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menu_btn.setText(_translate("Form", "菜单"))
        self.about_menu_btn.setText(_translate("Form", "关于"))
        self.exit_menu_btn.setText(_translate("Form", "退出"))
        self.reset_menu_btn.setText(_translate("Form", "重置"))
        self.label.setText(_translate("Form", "账    号："))
        self.label_3.setText(_translate("Form", "密    码："))
        self.label_2.setText(_translate("Form", "确认密码："))
        self.register_btn.setText(_translate("Form", "注册"))
import image_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
