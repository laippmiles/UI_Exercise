import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QWidget,QFileDialog
from PyQt5.QtGui import *
from ex5_ToolBar_and_Act import Ui_MainWindow
from displayData import tableDialog
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("污水故障诊断分析系统")
        self.table = tableDialog()
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.fileNewAction.triggered.connect(self.saveAs)
        self.LoadFileName = None
        self.SaveFileName = None
        self.data = None
        self.feature = None
        self.train_data = None
        self.train_lebel = None
        self.resize(500,500)
        self.setFixedSize(500,500)

    def openMsg(self):
        # 这个是固定写法
        #改写成了可以加载文件的形式
        self.LoadFileName,fileType = QFileDialog.getOpenFileName(self,"打开","D:\桌面"," Csv Files (*.csv)")
        #https: // blog.csdn.net / a359680405 / article / details / 45166271
        print(self.LoadFileName,fileType)
        if self.LoadFileName and fileType:
            self.statusbar.showMessage('Loading '+ self.LoadFileName)
            from pandas import read_csv
            self.data = read_csv(self.LoadFileName)
            self.feature = list(self.data.columns.values)
            # 提取特征名
            self.train_data = self.data.values[:, 4:]
            # 训练数据
            self.train_data_label = self.data.values[:, 3]
            # 训练标签
            print(list(self.feature))
            #注意getOpenFileName函数返回两个变量，只接一个变量的话程序会崩溃的
            self.statusbar.showMessage('Load '+ self.LoadFileName + ' complete!')
            print("Display Data")
            self.disData()
            #显示文件地址

    def saveAs(self):
        self.SaveFileName, savepro = QFileDialog.getSaveFileName(self, "打开", "D:\桌面", " Csv Files (*.csv)")
        print(self.SaveFileName, savepro)
        if self.LoadFileName and savepro:
            self.statusbar.showMessage('Saving ' + self.SaveFileName)
            from save_as import save_as
            save_as(self.data.values,self.SaveFileName)
            self.statusbar.showMessage('Save ' + self.SaveFileName + ' complete!')

    def disData(self):
        self.table.setWindowTitle("载入数据_From_" + self.LoadFileName)
        self.table.model.setHorizontalHeaderLabels(list(self.feature))
        from numpy import shape
        sizeOfData = list(shape(self.data.values))
        for row in range(sizeOfData[0]):
            for column in range(sizeOfData[1]):
                print("B")
                item = QStandardItem(str(self.data.values[row,column]))
                self.table.model.setItem(row, column, item)
        self.table.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())