from PyQt5.Qt import *
from Resources.Register import Ui_Form


class RegisterPanel(QWidget, Ui_Form):
    exit_signal = pyqtSignal()  # 点击退出按钮时发生该信号
    register_account_pwd_signal = pyqtSignal(str, str)  # 当点击注册按钮时发射该信号

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 不加这句话背景出不来
        self.setupUi(self)  # 初始化界面

        self.animation_target = [self.about_menu_btn, self.exit_menu_btn, self.reset_menu_btn]
        self.animation_target_pos = [target.pos() for target in self.animation_target]


    def create_animation(self, direction):
        """
        创建菜单动画
        :param direction:
        :return:
        """
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_target):
            animation = QPropertyAnimation(target, b"pos")
            animation.setStartValue(self.main_menu_btn.pos())
            animation.setEndValue(self.animation_target_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce if direction == 0 else QEasingCurve.Linear)
            animation_group.addAnimation(animation)

        animation_group.setDirection(direction)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def show_hide_menu(self, checked):
        """
        当点击主菜单时创建动画
        :param checked:
        :return:
        """
        self.create_animation(checked)

    def about_lk(self):
        """
        关于菜单
        :return:
        """
        pass

    def exit_panel(self):
        """
        推出菜单，当点击推出按钮时向外界发射一个信号
        :return:
        """
        self.exit_signal.emit()

    def reset(self):
        """
        重置菜单
        :return:
        """
        pass

    def check_register(self):
        """
        注册按钮，当点击登陆按钮时向外界发射一个信号
        :return:
        """
        # self.register_account_pwd_signal.emit()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = RegisterPanel()
    window.show()

    sys.exit(app.exec_())
