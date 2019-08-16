# -*- coding: utf-8 -*-
from googlesearch import search
import wget

print ('Jamerson Walderson | github.com/JamersonWalderson | jamersonwalderson@gmail.com')
print ("# MODO DE USAR:"
       "\n 1 - crie uma pasta vazia onde ficarão os PDF's que serão baixados"
       "\n 2 - Execute o programa"
       "\n 3 - Entre com o conteudo que deseja procurar e a quantidade de itens que será baixado")

find = input('O que deseja buscar? ')+' filetype:pdf'
size = int(input('Quantos arquivos deseja? '))


for url in search(find+' filetype:pdf', stop=size):
    try:
        wget.download(url)
    except:
        print("\nAlgo de errado não está certo")
