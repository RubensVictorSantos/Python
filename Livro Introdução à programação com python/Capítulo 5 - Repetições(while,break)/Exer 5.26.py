print("Exercício 5.26 Escreva um programa que calcule o resto\n"
"da divisão inteira entre dois números. Utilize apenas as\n"
"operações de soma e subtração para calcular o resultado.\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
cont = 0

while cont < num1:

    cont = cont + num2

resto = cont - num1
print("Resto da divisão = %d" % resto)
