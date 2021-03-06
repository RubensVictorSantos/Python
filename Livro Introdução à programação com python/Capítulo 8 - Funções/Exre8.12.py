print('Exercício 8.12 Escreva uma função que receba uma string e uma lista.\n'
'A função deve comparar a string passada com os elementos da lista, também\n'
'como parâmetro. Retorne verdadeiro se a string for encontrada dentro da\n'
'lista, e falso em caso contrário.\n')

def cmp(L,str):
    for e in L:
        if str.find(e) >= 0:
            print(True)
            return
    print(False)

#-------------------------------------------------------------------------
"""Lista = ['pera','maçã','kiwi']
string = 'banana'
cmp(Lista,string)"""
