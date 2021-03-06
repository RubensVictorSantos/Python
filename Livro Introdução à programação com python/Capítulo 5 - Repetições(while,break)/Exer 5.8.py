print("Exercício 5.8 Escreva um programa que leia dois números. Imprima o\n"
"resultado da multiplicação do primeiro pelo segundo. Ultilize apenas os operadores\n"
"de soma e subtração para calcular o resultado. Lembre-se de que podemos entender\n"
"a multiplicação de dois números como somas sucessivas de um deles. Assim, 4x5 = 5\n"
" + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. \n")

n1 = int(input(" Digite o primeiro número:"))
n2 = int(input(" Digite o segundo número:"))
Resul = 0
cont = 0

while cont < n1:

    Resul = Resul + n2

    cont = cont + 1
print("\n Resultado = " ,Resul)
