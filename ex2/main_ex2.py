from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from ex2 import Ui_MainWindow

class Layout(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(Layout,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    #很奇怪，杠掉上一句的话程序会运行两遍
    def on_dis_shouyi_clicked(self):
        #这个是固定写法
        print('收益_min:',self.return_min.text())
        print('收益_max:', self.return_max.text())

    @pyqtSlot()
    #一个@pyqtSlot()只管一个按钮
    def on_dis_zuidahuiche_clicked(self):
        #这个是固定写法
        #格式大致为on_该按钮名字_clicked（self）:
        print('最大回撤_min:',self.return_maxdrawdown_min.text())
        print('收益_max:', self.return_maxdrawdown_max.text())

    @pyqtSlot()
    def on_dis_sharp_clicked(self):
        #这个是固定写法
        print('sharp_min:',self.return_sharp_min.text())
        print('sharp_max:', self.return_sharp_max.text())

if __name__ == "__main__":
    import sys

app = QApplication(sys.argv)
ui = Layout()
ui.show()
sys.exit(app.exec_())