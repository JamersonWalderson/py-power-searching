import sys
from PyQt5 import QtWidgets, uic
from search import Search


janela = QtWidgets.QApplication(sys.argv)
interface = uic.loadUi('main-designer.ui')
# procurar = Search('digimon',5)

def listar():
    pesquisa = interface.txtPesquisar.text()
    procurar = Search(pesquisa,5)   
    #print (pesquisa)
    interface.listVisualizar.addItems(procurar.buscar())

interface.btProcurar.clicked.connect(listar)


interface.show()
sys.exit(janela.exec())