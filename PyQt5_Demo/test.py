from PyQt5.Qt import *

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login_panel = QWidget()
    login_panel.resize(200, 200)


    reg = QWidget(login_panel)
    reg.move(50, 50)
    reg.setObjectName("reg")
    reg.setStyleSheet("""
    QWidget#reg{
        background-color:gray;
    }
    
    """)
    reg.show()
    login_panel.show()
    sys.exit(app.exec_())