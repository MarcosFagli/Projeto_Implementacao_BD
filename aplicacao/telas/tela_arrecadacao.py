# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_arrecadacao.ui',
# licensing of 'tela_arrecadacao.ui' applies.
#
# Created: Wed Jul 10 21:42:01 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(345, 171)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 59, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 59, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 59, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.label_5.setObjectName("label_5")
        self.edit_qtd = QtWidgets.QLineEdit(Form)
        self.edit_qtd.setGeometry(QtCore.QRect(100, 130, 113, 23))
        self.edit_qtd.setObjectName("edit_qtd")
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(220, 130, 80, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.label_tipo = QtWidgets.QLabel(Form)
        self.label_tipo.setGeometry(QtCore.QRect(60, 10, 221, 16))
        self.label_tipo.setText("")
        self.label_tipo.setObjectName("label_tipo")
        self.label_nome = QtWidgets.QLabel(Form)
        self.label_nome.setGeometry(QtCore.QRect(70, 30, 211, 16))
        self.label_nome.setText("")
        self.label_nome.setObjectName("label_nome")
        self.label_marca = QtWidgets.QLabel(Form)
        self.label_marca.setGeometry(QtCore.QRect(70, 50, 281, 16))
        self.label_marca.setText("")
        self.label_marca.setObjectName("label_marca")
        self.label_valor = QtWidgets.QLabel(Form)
        self.label_valor.setGeometry(QtCore.QRect(100, 70, 81, 16))
        self.label_valor.setText("")
        self.label_valor.setObjectName("label_valor")
        self.label_unidade = QtWidgets.QLabel(Form)
        self.label_unidade.setGeometry(QtCore.QRect(220, 70, 81, 16))
        self.label_unidade.setText("")
        self.label_unidade.setObjectName("label_unidade")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Nome:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Marca:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Tipo:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Quantidade:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Arrecadado:", None, -1))
        self.btn_ok.setText(QtWidgets.QApplication.translate("Form", "OK", None, -1))

