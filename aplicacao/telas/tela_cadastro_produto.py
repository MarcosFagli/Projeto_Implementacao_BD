# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro_produto.ui',
# licensing of 'tela_cadastro_produto.ui' applies.
#
# Created: Wed Jul 10 23:08:40 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 171)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 59, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 59, 15))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 59, 15))
        self.label_8.setObjectName("label_8")
        self.box_tipo = QtWidgets.QComboBox(Form)
        self.box_tipo.setGeometry(QtCore.QRect(60, 10, 141, 23))
        self.box_tipo.setObjectName("box_tipo")
        self.box_tipo.addItem("")
        self.box_tipo.addItem("")
        self.box_tipo.addItem("")
        self.edit_nome = QtWidgets.QLineEdit(Form)
        self.edit_nome.setGeometry(QtCore.QRect(60, 38, 191, 20))
        self.edit_nome.setObjectName("edit_nome")
        self.edit_marca = QtWidgets.QLineEdit(Form)
        self.edit_marca.setGeometry(QtCore.QRect(60, 60, 191, 20))
        self.edit_marca.setObjectName("edit_marca")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 91, 16))
        self.label_2.setObjectName("label_2")
        self.box_unidade = QtWidgets.QComboBox(Form)
        self.box_unidade.setGeometry(QtCore.QRect(140, 110, 79, 23))
        self.box_unidade.setObjectName("box_unidade")
        self.box_unidade.addItem("G")
        self.box_unidade.addItem("KG")
        self.box_unidade.addItem("L")
        self.box_unidade.addItem("UN")
        self.box_unidade.addItem("LATA")
        self.box_unidade.addItem("ML")
        self.edit_quantidade = QtWidgets.QLineEdit(Form)
        self.edit_quantidade.setGeometry(QtCore.QRect(90, 140, 131, 23))
        self.edit_quantidade.setObjectName("edit_quantidade")
        self.btn_cadastrar = QtWidgets.QPushButton(Form)
        self.btn_cadastrar.setGeometry(QtCore.QRect(250, 140, 80, 23))
        self.btn_cadastrar.setObjectName("btn_cadastrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Marca:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Nome:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "Tipo:", None, -1))
        self.box_tipo.setItemText(0, QtWidgets.QApplication.translate("Form", "Alimento", None, -1))
        self.box_tipo.setItemText(1, QtWidgets.QApplication.translate("Form", "Higiente", None, -1))
        self.box_tipo.setItemText(2, QtWidgets.QApplication.translate("Form", "Limpeza", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Unidade de Medida:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Quantidade:", None, -1))
        self.btn_cadastrar.setText(QtWidgets.QApplication.translate("Form", "Cadastrar", None, -1))

