from PyQt5.Qt import *
from Resources.login_ui import Ui_Form


class LoginPanel(QWidget, Ui_Form):
    show_register_panel_signal = pyqtSignal()  # 当点击注册时发生该信号
    check_login_signal = pyqtSignal(str, str)  # 当点击登陆按钮时发射该信号

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)  # 初始化界面
        self.set_gif_move()  # 初始化gif动画

    def set_gif_move(self):
        movie = QMovie(":/newPrefix/Images/xue.gif")
        self.login_top_bg_label.setMovie(movie)
        # movie.setScaledSize(QSize(400, 200))
        movie.start()

    def show_register_panel(self):
        """
        当点击注册账号时向外界发射信号
        :return:
        """
        self.show_register_panel_signal.emit()

    def enable_login_btn(self):
        """
        当账号和密码发生改变时调用该槽
        :return:
        """
        account = self.account_cb.currentText()
        pwd = self.pasw_le.text()
        print(account+":"+pwd)
        if account.strip() != "" and pwd.strip() != "":
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):
        """
        当点击登陆按钮时，向外界发射信号
        :return:
        """
        account = self.account_cb.currentText()
        pwd = self.pasw_le.text()
        self.check_login_signal.emit(account, pwd)

    def auto_login(self, checked):
        """
        自动登陆复选框状态改变时调用该槽
        :param checked:
        :return:
        """
        if checked:
            self.remember_pwd_cb.setChecked(True)

    def remember_pwd(self, checked):
        """
        记住密码复选框状态改变时调用该槽
        :param checked:
        :return:
        """
        if not checked:
            self.auto_login_cb.setChecked(False)

    def open_qq_link(self):
        pass

    def show_error_animation(self):
        """
        创建抖动动画
        :return:
        """
        animation = QPropertyAnimation(self.login_bottom, b"pos", self)
        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_bottom.pos())
        animation.setDuration(150)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = LoginPanel()
    window.show()

    sys.exit(app.exec_())
