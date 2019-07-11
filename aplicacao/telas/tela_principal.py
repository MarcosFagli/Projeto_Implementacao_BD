# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui',
# licensing of 'tela.ui' applies.
#
# Created: Wed Jul 10 20:58:20 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 110, 108, 16))
        self.label.setObjectName("label")
        self.edit_cb = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_cb.setGeometry(QtCore.QRect(124, 110, 171, 23))
        self.edit_cb.setObjectName("edit_cb")
        self.box_instituicao = QtWidgets.QComboBox(self.groupBox_2)
        self.box_instituicao.setGeometry(QtCore.QRect(80, 30, 211, 23))
        self.box_instituicao.setObjectName("box_instituicao")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.btn_ok = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ok.setGeometry(QtCore.QRect(310, 110, 80, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Arrecadação:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Código de Barras:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Instituição:", None, -1))
        self.btn_ok.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))

