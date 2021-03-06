print('Exercício 8.2 Escreva uma função que receba dois números\n'
'e retorne True se o primeiro número for múltiplo do segundo\n'
'Valores esperados:\n'
'múltiplo(8,4)==True\n'
'múltiplo(7,3)==False\n'
'múltiplo(5,5)==True\n')
def mul(a,b):
    if a%b == 0:
        print(True)
    else:
        print(False)
        return

    
mul(8,4)
mul(7,3)
mul(5,5)
