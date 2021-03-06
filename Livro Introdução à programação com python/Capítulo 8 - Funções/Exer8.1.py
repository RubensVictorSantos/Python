print('Exercício 8.1 Escreva um a função que retorne o maior de dois\n'
'números.'
'Valores esperados:\n'
'máximo(5,6)==6\n'
'máximo(2,1)==2\n'
'máximo(7,7)==7\n')
def maximo(a,b):
    if a > b:
        print("%d é o maior"% a)
        return
    else:
        print("%d é o maior"% b)
        return
    
maximo(5,6)
maximo(2,1)
maximo(7,7)
