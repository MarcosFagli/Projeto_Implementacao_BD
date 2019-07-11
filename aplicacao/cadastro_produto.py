import sys

from PySide2 import QtWidgets, QtCore

from telas.tela_cadastro_produto import Ui_Form

from conexao_bd import select, executa_cmd, insert, showdialog

class TelaCadastroProduto(QtWidgets.QWidget):
    def __init__(self, cod_barras, cod_inst, parent=None):
        super(TelaCadastroProduto, self).__init__()
        self.parent = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connectSignals()

        self.cb = cod_barras

    def connectSignals(self):
        self.ui.btn_cadastrar.clicked.connect(self.clica_cadastrar)

    def clica_cadastrar(self):
        codbarras = self.cb
        tipo = self.ui.box_tipo.currentText()
        nome = self.ui.edit_nome.text()
        marca = self.ui.edit_marca.text()
        unidade = self.ui.box_unidade.currentText()
        quantidade = self.ui.edit_quantidade.text()
        x = executa_cmd(f"INSERT INTO produto (codBarras, tipo, nome, marca, unidadeMedida, valorMedida) VALUES ('{str(codbarras)}', '{str(tipo)}', '{str(nome)}', '{str(marca)}', '{str(unidade)}', '{str(quantidade)}');")
        showdialog("Sucesso!", "Produto cadastrado!")
        self.hide()

