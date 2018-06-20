import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QWidget,QFileDialog
from ex5_ToolBar_and_Act import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.fileName = None
        self.data = None
        self.feature = None
        self.train_data = None
        self.train_lebel = None

    def openMsg(self):
        # 这个是固定写法
        #改写成了可以加载文件的形式
        self.fileName,fileType = QFileDialog.getOpenFileName(self,"打开","D:\桌面"," Csv Files (*.csv)")
        #https: // blog.csdn.net / a359680405 / article / details / 45166271
        print(self.fileName,fileType)
        if self.fileName:
            self.statusbar.showMessage('Loading '+ self.fileName)
            from pandas import read_csv
            self.data = read_csv(self.fileName)
            self.feature = list(self.data.columns.values)
            # 提取特征名
            self.train_data = self.data.values[:, 4:]
            # 训练数据
            self.train_data = self.data.values[:, 3]
            # 训练标签
            print(list(self.feature))
            #注意getOpenFileName函数返回两个变量，只接一个变量的话程序会崩溃的
            self.statusbar.showMessage('Load '+ self.fileName + ' complete!')
            #显示文件地址

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())