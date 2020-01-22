# https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
# https://tiforadacaixa.blogspot.com/2019/09/pyside2-pyqt-estruturando-projeto-em-mvc.html

from PyQt5 import QtWidgets, uic
from modelProcurar import *
from threading import Thread
import sys

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main-designer.ui', self)

        # findchield() = serve para encontrar o modulo do item
        self.btProcurar = self.findChild(QtWidgets.QPushButton, 'btProcurar')
        self.btProcurar.clicked.connect(self.realizar_pesquisa)

        self.btLimpar = self.findChild(QtWidgets.QPushButton, 'btLimpar')
        self.btLimpar.clicked.connect(self.limpar_tela)

        self.btBaixar = self.findChild(QtWidgets.QPushButton, 'btBaixar')
        self.btBaixar.clicked.connect(self.baixar_item_selecionado)

        self.btbaixar_tudo = self.findChild(QtWidgets.QPushButton, 'btBaixarTudo')
        self.btbaixar_tudo.clicked.connect(self.baixar_tudo)

        # Armazena o valor digitado no QLineEdit na variavel assunto_da_pesquisa
        self.assunto_da_pesquisa = self.findChild(QtWidgets.QLineEdit, 'txtPesquisar')
        

        self.show()

    def tema_pesquisa(self, assunto_pesquisado):
        assunto_pesquisado = assunto_pesquisado
        return assunto_pesquisado

    def realizar_pesquisa(self):
        encontrados = []
        assunto_pesquisado = self.txtPesquisar.text()
        procurar = ModelProcurar(assunto_pesquisado,20)
        encontrados.extend(procurar.buscar())
        self.listVisualizar.addItems(encontrados)
        return encontrados

    def limpar_tela(self):
        self.listVisualizar.clear()
    
    def baixar_item_selecionado(self):
        print ('#baixar')
        # codigo
    
    def baixar_tudo(self):
        # a variável assunto recebe o valor digitado no QlineEdit
        assunto = self.assunto_da_pesquisa.text()
        baixar_lista = ModelProcurar(assunto, 20)
        baixar_lista.baixarTudo()




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()