import webbrowser
#from tes import *
#from gui import *

# Mostrar url usando o navegador padrão. Se o novo for 0, a url é aberto na mesma janela do navegador,
# se possível. Se é novo 1, uma nova janela do navegador é aberto, se possível.

class Navegar:

    def abrirnavegador(self, conteudo):
        webbrowser.open('https://www.google.com/search?q=' + conteudo, new=0, autoraise=True)

'''
if __name__=="__main__":
    n = Navegar()
    n.abrirnavegador('pantera negra')
'''