import sys

from PyQt5 import QtWidgets

from ex_1 import Ui_MainWindow  # 导入生成form.py里生成的类


class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())