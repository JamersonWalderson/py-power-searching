# search.py
# -*- coding: utf-8 -*-
'''
    jamersonwalderson@gmail.com
    Conteúdo usado para suporte
    http://pythonclub.com.br/introducao-classes-metodos-python-basico.html
'''
from googlesearch import search
from threading import Thread
import platform
import wget


class ModelProcurar:
    
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
    
    
    def baixarTudo(self):
        baixados_com_sucesso = 0      
        for urls in search(self.procurar, num=1, start=0, stop=self.qt_itens, pause=2.0):
            try:
                baixados_com_sucesso+=1
                print ( baixados_com_sucesso )
                wget.download(urls)
            except:
                print ('O download de ', urls, 'falhou.')
    
    def baixarSelecionado(self, download_item):
        wget.download(download_item)

    def testando(self):
        print ('funfo')

'''
teste = Search('digimon',5)
print (teste.buscar())
#procurar.listar()
# print (str())
'''
