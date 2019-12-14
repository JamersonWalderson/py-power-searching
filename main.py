from search import Search

procurar = input ('O que deseja procurar: ')
qt_itens = input ('Quantidade de itens: ')
s = Search(procurar, qt_itens)
s.listar()