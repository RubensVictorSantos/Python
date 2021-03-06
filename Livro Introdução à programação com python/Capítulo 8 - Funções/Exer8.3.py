print('Exercício 8.3 Escreva uma função que receba o lado(l)\n'
'de um quadrado e retorne sua área (A=lado²).\n'
'Valores esperados:\n'
'área_quadrado(4)==16\n'
'área_quadrado(9)==81\n')

def area_quadrado(x):
    A = x**2
    print("Raiz quadrada de %d = %d" %(x, A))
    return

area_quadrado(4)
area_quadrado(9)
