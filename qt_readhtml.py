import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QMessageBox, QApplication
from PyQt5.QtCore import QCoreApplication
import readhtml

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        def helloworld():
            print('hello, world')

        ##创建窗口：
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('FirstPyQtProgram')

        ##创建按钮：
        qb = QPushButton('Button', self)##创建一个按钮
        qb.resize(qb.sizeHint())
        qb.move(50, 50)
        
        ##链接按钮行为：
        qb.clicked.connect(readhtml.readhtml)

        ##创建按钮提示框：
        qb.setToolTip('This is a <b>HelloWorld</b> Button')

        self.show()


if __name__ == '__main__':


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
