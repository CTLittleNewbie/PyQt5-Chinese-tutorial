from PyQt5.Qt import *
from Resources.calculate import Ui_Form


class CalculatePanel(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = CalculatePanel()
    window.show()

    sys.exit(app.exec_())
