import sys

from PySide2 import QtWidgets, QtCore

from telas.tela_principal import Ui_MainWindow

from arrecadacao import TelaArrecadacao
from cadastro_produto import TelaCadastroProduto

from conexao_bd import select, executa_select

class TelaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignals()
        self.carrega_box()

    def eventFilter(self, obj, ev):
        """Filter event wheel.
        """

        if ev.type() == QtCore.QEvent.Wheel:
            return True
        return False

    def connectSignals(self):
        self.ui.btn_ok.clicked.connect(self.clica_ok_principal)

    def someAction(self):
        self.ui.lineEdit.setText("Hello World")

    def carrega_box(self):
        self.bairros = {bairro[1]: bairro[0] for bairro in executa_select("select codinst, endbairro from bairro")}
        self.ui.box_instituicao.addItems(list(self.bairros.keys()))

    def clica_ok_principal(self):
        cb = self.ui.edit_cb.text()
        produto = executa_select(f"select * from produto where codbarras = '{cb}'")
        bairro = self.ui.box_instituicao.currentText()
        cod_inst = self.bairros[bairro]
        if produto:
            self.tela_arrecadacao = TelaArrecadacao(cod_inst, produto, parent=self)
            self.tela_arrecadacao.show()
        else:
            self.tela_cadastro_produto = TelaCadastroProduto(cb, cod_inst, parent=self)
            self.tela_cadastro_produto.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = TelaPrincipal()
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
