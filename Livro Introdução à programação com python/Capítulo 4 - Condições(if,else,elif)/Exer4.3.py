print("Exercício 4.3 Escreva um programa que leia três números e que imprima o"
" maior  e o menor. \n ")

A = float(input("Digite o Valor de A:"))
B = float(input("Digite o Valor de B:"))
C = float(input("Digite o Valor de C:"))
if A > B and A > C:
    print ("A tem o valor maior")
elif A < B and B > C:
        print ("B tem o valor maior")
elif C > B and C > A:
    print ("C tem o valor maior")
else:
    print("Não pode digitar valores iguais!")
