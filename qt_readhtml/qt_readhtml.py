import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QMessageBox, QApplication
from PyQt5.QtCore import QCoreApplication

import os
import getdata

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        def readhtml():
            url ='file:///C:/Users/zk/Desktop/readhtml/html-%E6%80%9D%E6%8B%93%E5%8A%9B/E15_071613.html'
            getdata.getdata(url)
            print('完成')
            
        ##创建窗口：
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('FirstPyQtProgram')

        ##创建按钮：
        qb = QPushButton('ReadHtml', self)##创建一个按钮
        qb.resize(qb.sizeHint())
        qb.move(50, 50)
        
        ##链接按钮行为：
        qb.clicked.connect(readhtml)

        self.show()


if __name__ == '__main__':


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
