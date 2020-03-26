# https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
# https://tiforadacaixa.blogspot.com/2019/09/pyside2-pyqt-estruturando-projeto-em-mvc.html
# https://www.tutorialspoint.com/pyqt/pyqt_qcombobox_widget.htm
# https://www.seomartin.com/como-pesquisar-arquivos-publicos-internet-google/
# https://docs.python.org/pt-br/3/tutorial/modules.html#packages


from PyQt5 import QtWidgets, uic
from model.navegar import Navegar
import webbrowser
from threading import Thread
import sys

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('view/simple-design.ui', self)

        # findchield() = serve para encontrar o modulo do item
        self.btGoogle = self.findChild(QtWidgets.QPushButton, 'btGoogle')
        self.btGoogle.clicked.connect(self.pesquisa_google)

        self.btGoogleDrive = self.findChild(QtWidgets.QPushButton, 'btGoogleDrive')
        self.btGoogleDrive.clicked.connect(self.pesquisa_google_drive)

        self.bt_github = self.findChild(QtWidgets.QPushButton, 'bt_github')
        self.bt_github.clicked.connect(self.meu_github)
        # Armazena o valor digitado no QLineEdit na variavel assunto_da_pesquisa
        self.txtEntrada = self.findChild(QtWidgets.QLineEdit, 'txtEntrada')

        self.lbTeste = self.findChild(QtWidgets.QLabel, 'lbTeste')

        self.cb_google.currentIndexChanged.connect(self.pesquisa_google)
        self.cb_google_drive.currentIndexChanged.connect(self.pesquisa_google_drive)

        self.show()

    def pesquisa_google(self):
        tipo = str()
        if (self.cb_google.itemText(self.cb_google.currentIndex()) == 'Documento'):
            tipo = 'pdf'
        elif (self.cb_google.itemText(self.cb_google.currentIndex()) == 'Audio'):
            tipo = 'mp3'
        elif (self.cb_google.itemText(self.cb_google.currentIndex()) == 'Video'):
            tipo = 'mp4'
        assunto_pesquisa_google = self.txt_entrada_google.text() + ' filetype:' + tipo
        n = Navegar()
        n.abrirnavegador(assunto_pesquisa_google)
    
    def pesquisa_google_drive(self):
        tipo = str()
        if (self.cb_google_drive.itemText(self.cb_google_drive.currentIndex()) == 'Geral'):
            tipo = 'inurl:docs.google.com/file/d'
        elif (self.cb_google_drive.itemText(self.cb_google_drive.currentIndex()) == 'Seminarios'):
            tipo = 'docs.google.com/presentation/d'
        elif (self.cb_google_drive.itemText(self.cb_google_drive.currentIndex()) == 'Desenhos'):
            tipo = 'docs.google.com/drawings/d'       
        assunto_pesquisa_googledrive = self.txt_entrada_google_drive.text() + tipo
        n = Navegar()
        n.abrirnavegador(assunto_pesquisa_googledrive)

    def meu_github(self):
        webbrowser.open('https://github.com/JamersonWalderson', new=0, autoraise=True)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()