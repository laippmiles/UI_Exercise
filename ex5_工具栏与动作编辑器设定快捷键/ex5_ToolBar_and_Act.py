# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex5_ToolBar_and_Act.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setTearOffEnabled(False)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileCloseAction = QtWidgets.QAction(MainWindow)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.fileSaveAction = QtWidgets.QAction(MainWindow)
        self.fileSaveAction.setObjectName("fileSaveAction")
        self.fileNewAction = QtWidgets.QAction(MainWindow)
        self.fileNewAction.setObjectName("fileNewAction")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menu_F.addAction(self.fileOpenAction)
        self.menu_F.addAction(self.fileCloseAction)
        self.menu_F.addAction(self.fileSaveAction)
        self.menu_F.addAction(self.fileNewAction)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(E)"))
        self.fileOpenAction.setText(_translate("MainWindow", "打开(Shift+O)"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Shift+O"))
        self.fileCloseAction.setText(_translate("MainWindow", "关闭(Shift+C)"))
        self.fileCloseAction.setShortcut(_translate("MainWindow", "Shift+C"))
        self.fileSaveAction.setText(_translate("MainWindow", "保存(Ctrl+S)"))
        self.fileSaveAction.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.fileNewAction.setText(_translate("MainWindow", "另存为(Shift+S)"))
        self.fileNewAction.setToolTip(_translate("MainWindow", "新建"))
        self.fileNewAction.setShortcut(_translate("MainWindow", "Shift+S"))
        self.addWinAction.setText(_translate("MainWindow", "新建窗体"))
        self.addWinAction.setToolTip(_translate("MainWindow", "新建窗体"))

