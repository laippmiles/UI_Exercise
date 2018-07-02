# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog

from Ui_pandas_pyqt import Ui_MainWindow

from qtpandas.models.DataFrameModel import DataFrameModel
from pandas import read_csv

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        '''初始化pandasqt'''
        widget = self.pandastablewidget
        widget.resize(600, 500) # 如果对部件尺寸大小不满意可以在这里设置


        self.model = DataFrameModel() # 设置新的模型
        widget.setViewModel(self.model)

        self.LoadFileName = None

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        初始化pandas
        """
        self.model.setDataFrame(self.dataframe_original)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        保存数据
        """
        data = ui.dataframe.values
        print(data)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.LoadFileName, fileType = QFileDialog.getOpenFileName(ui, "打开", "D:\桌面", " Csv Files (*.csv)")
    if ui.LoadFileName and fileType:
        ui.dataframe = read_csv(ui.LoadFileName)
        ui.dataframe_original = ui.dataframe.copy()  # 备份原始数据
        ui.model.setDataFrame(ui.dataframe)
    ui.show()
    sys.exit(app.exec_())
