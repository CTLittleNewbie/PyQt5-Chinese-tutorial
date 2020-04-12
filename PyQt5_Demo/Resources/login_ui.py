# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login_top_bg_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_top_bg_label.sizePolicy().hasHeightForWidth())
        self.login_top_bg_label.setSizePolicy(sizePolicy)
        self.login_top_bg_label.setMaximumSize(QtCore.QSize(16777215, 120))
        self.login_top_bg_label.setText("")
        self.login_top_bg_label.setObjectName("login_top_bg_label")
        self.verticalLayout_2.addWidget(self.login_top_bg_label)
        self.verticalLayout.addWidget(self.widget)
        self.login_bottom = QtWidgets.QWidget(Form)
        self.login_bottom.setObjectName("login_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_bottom)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 10)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.login_bottom)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 25))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setContentsMargins(0, 18, 0, 16)
        self.formLayout.setHorizontalSpacing(63)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.account_cb = QtWidgets.QComboBox(self.widget_3)
        self.account_cb.setMinimumSize(QtCore.QSize(0, 30))
        self.account_cb.setStyleSheet("QComboBox{\n"
"    font-size:15px;\n"
"    background:transparent;    \n"
"    border-bottom:1px solid lightgray;\n"
"    border-style:outset;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom:1px solid rgb(18,183,245);\n"
"}\n"
"QComboBox::down-arrow { \n"
"    width: 40px;\n"
"    height:25px;\n"
"    background-color: transparent;     \n"
"    image: url(:/newPrefix/Images/1.png); \n"
"} \n"
"QComboBox::drop-down { \n"
"    width: 40px;\n"
"    height:25px;\n"
"    background-color: transparent;     \n"
"} \n"
"QComboBox QAbstractItemView { \n"
"    \n"
"    min-height:20px;\n"
"    \n"
"} \n"
"QComboBox QAbstractItemView:item { \n"
"    \n"
"    color:lightblue;\n"
"    \n"
"}\n"
"")
        self.account_cb.setEditable(True)
        self.account_cb.setObjectName("account_cb")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Images/bg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon, "")
        self.account_cb.addItem(icon, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.account_cb)
        self.pasw_le = QtWidgets.QLineEdit(self.widget_3)
        self.pasw_le.setMinimumSize(QtCore.QSize(0, 30))
        self.pasw_le.setStyleSheet("QLineEdit{\n"
"    background:transparent;    \n"
"    border-bottom:1px solid lightgray;\n"
"    border-style:outset;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom:1px solid rgb(18,183,245);\n"
"}")
        self.pasw_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pasw_le.setClearButtonEnabled(True)
        self.pasw_le.setObjectName("pasw_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.pasw_le)
        self.auto_login_cb = QtWidgets.QCheckBox(self.widget_3)
        self.auto_login_cb.setMinimumSize(QtCore.QSize(0, 30))
        self.auto_login_cb.setObjectName("auto_login_cb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.auto_login_cb)
        self.remember_pwd_cb = QtWidgets.QCheckBox(self.widget_3)
        self.remember_pwd_cb.setMinimumSize(QtCore.QSize(0, 30))
        self.remember_pwd_cb.setMaximumSize(QtCore.QSize(70, 16777215))
        self.remember_pwd_cb.setObjectName("remember_pwd_cb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.remember_pwd_cb)
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.login_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(33,174,250);\n"
"    border-radius:10px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(72,203,250);\n"
"    \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(85,85,250);\n"
"    \n"
"}\n"
"QPushButton:disabled{\n"
"    background-color:rgb(149, 149, 149);\n"
"    \n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Images/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setIconSize(QtCore.QSize(25, 25))
        self.login_btn.setObjectName("login_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.login_btn)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.login_bottom)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 68))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/Images/3.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.login_bottom)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.show_register_panel)
        self.account_cb.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.pasw_le.textChanged['QString'].connect(Form.enable_login_btn)
        self.pushButton_2.clicked.connect(Form.open_qq_link)
        self.login_btn.clicked.connect(Form.check_login)
        self.auto_login_cb.clicked['bool'].connect(Form.auto_login)
        self.remember_pwd_cb.clicked['bool'].connect(Form.remember_pwd)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "注册账号"))
        self.account_cb.setItemText(0, _translate("Form", "12132324"))
        self.account_cb.setItemText(1, _translate("Form", "fsdxvxxvb"))
        self.auto_login_cb.setText(_translate("Form", "自动登陆"))
        self.remember_pwd_cb.setText(_translate("Form", "记住密码"))
        self.login_btn.setText(_translate("Form", "安全登陆"))
import image_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
