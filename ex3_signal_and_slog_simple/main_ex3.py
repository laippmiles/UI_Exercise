from PyQt5.QtWidgets import QApplication , QMainWindow
from ex3_signal_and_slog_simple import Ui_Form
class MainWindow(QMainWindow,Ui_Form):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

#固定写法，都这么写，死记硬背吧
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())