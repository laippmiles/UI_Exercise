# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class tableDialog(QDialog):
    """docstring for myDialog"""
    def __init__(self, arg=None):
        super(tableDialog, self).__init__(arg)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.resize(800,400);
        self.model=QStandardItemModel();

        self.tableView=QTableView();
        self.tableView.setModel(self.model)
        #self.tableView.setColumnWidth(100,100)
        #下面代码让表格100填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        #self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout=QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)