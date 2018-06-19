import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QWidget,QFileDialog
from ex5_ToolBar_and_Act import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        # 这个是固定写法
        file,fileType = QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*) ;; Text Files (*.txt)")
        #https: // blog.csdn.net / a359680405 / article / details / 45166271
        print(file,fileType)
        #注意getOpenFileName函数返回两个变量，只接一个变量的话程序会崩溃的
        self.statusbar.showMessage(file)
        #显示文件地址

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())