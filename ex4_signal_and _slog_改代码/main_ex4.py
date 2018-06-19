from PyQt5.QtCore import pyqtSlot#要用单击输出变量要用这个
from PyQt5.QtWidgets import QApplication , QMainWindow
from MainWinSignalSlog03 import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)

        self.label.setVisible(False)
        self.lineEdit.setEnabled(False)

    @ pyqtSlot()
        # 很奇怪，杠掉上一句的话程序会运行两遍
    def on_output_clicked(self):
        # 这个是固定写法
        a = self.lineEdit.text()
        print('你输入了:', a)

#固定写法，都这么写，死记硬背吧
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())