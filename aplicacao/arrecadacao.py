import sys

from datetime import date
from PySide2 import QtWidgets, QtCore

from telas.tela_arrecadacao import Ui_Form

from conexao_bd import select, executa_cmd, insert, showdialog

class TelaArrecadacao(QtWidgets.QWidget):
    def __init__(self, cod_inst, produto, parent=None):
        super(TelaArrecadacao, self).__init__()
        self.parent = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connectSignals()

        self.codinst = cod_inst
        self.produto = produto

        self.ui.label_tipo.setText(str(produto[0][1]))
        self.ui.label_nome.setText(str(produto[0][2]))
        if produto[0][3] is not None:
            self.ui.label_marca.setText(str(produto[0][3]))
        self.ui.label_unidade.setText(str(produto[0][4]))
        self.ui.label_valor.setText(str(produto[0][5]))

    def connectSignals(self):
        self.ui.btn_ok.clicked.connect(self.clica_ok_arrecadacao)

    def clica_ok_arrecadacao(self):
        codbarras = self.produto[0][0]
        quantidade = self.ui.edit_qtd.text()
        data = date.today().strftime("%Y-%m-%d")

        x = executa_cmd(f"INSERT INTO campanhaArrecadacao (codBarras, codInst, quantidade, data) VALUES ('{str(codbarras)}', {str(self.codinst)}, {str(quantidade)}, '{str(data)}');")
        showdialog("Sucesso!", "Quantidade arrecadada cadastrada com sucesso!")
        self.parent.ui.edit_cb.setText("")
        self.hide()


