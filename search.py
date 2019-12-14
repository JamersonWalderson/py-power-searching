'''
    jamersonwalderson@gmail.com
    Conteúdo usado para suporte
    http://pythonclub.com.br/introducao-classes-metodos-python-basico.html
'''
from googlesearch import search
import wget

class Search:
    
    def __init__(self, procurar, qt_itens):
        self.procurar = procurar + 'filetype:pdf'
        self.qt_itens = qt_itens


       

    def buscar(self):
        # procurar = input('O que deseja buscar? ') + ' filetype:pdf'
        # qt_itens = int (input('Quantidade de resultados: '))
        # num =   int(input("Quantantidadede resultados a ser buscado: "))
        list_url = [] 

        for urls in search(self.procurar, num=1, start=0, stop=self.qt_itens, pause=2.0):
            list_url.append(urls)
        
        return list_url
    

'''
teste = Search('digimon',5)
print (teste.buscar())
#procurar.listar()
# print (str())
'''
