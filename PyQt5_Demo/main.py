from PyQt5.Qt import *
from login_panel import LoginPanel
from Register_Panel import RegisterPanel
from calculate_panel import CalculatePanel


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    login_panel = LoginPanel()  # 初始化登陆界面
    register_panel = RegisterPanel(login_panel)  # 初始化注册界面
    register_panel.move(0, login_panel.height())
    # register_panel.show()
    calculate_panel = CalculatePanel()  # 初始化计算机界面


    def show_register_panel():
        """
        创建注册界面出现动画
        :return:
        """
        animation = QPropertyAnimation(register_panel, b"pos", register_panel)
        animation.setStartValue(QPoint(0, login_panel.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    login_panel.show_register_panel_signal.connect(show_register_panel)

    def check_login(account, pwd):
        """
        登陆逻辑槽
        :param account:
        :param pwd:
        :return:
        """
        if account == "12132324" and pwd == "123456":
            print("登陆成功")
            calculate_panel.show()  # 显示计算机界面
            login_panel.hide()
        else:
            login_panel.show_error_animation()
    login_panel.check_login_signal.connect(check_login)

    def hide_register_panel():
        """
        注册界面隐藏动画
        :return:
        """
        animation = QPropertyAnimation(register_panel, b"pos", register_panel)
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_panel.width(), 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    register_panel.exit_signal.connect(hide_register_panel)

    login_panel.show()  # 显示登陆界面
    sys.exit(app.exec_())
