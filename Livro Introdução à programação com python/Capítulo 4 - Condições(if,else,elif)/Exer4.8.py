print("Exercício 4.8 Escreva um programa que leia dois números e que pergunte"
" qual operação você deseja realizar. Você deve poder calcular a soma (+), "
"subtração (-), multiplicação(*) e divisão(/). Exiba o resultado da operação"
" solicitada. \n")

num1 = int(input("Digite o 1º numero:"))
num2 = int(input("Digite o 2º numero:"))
operação = int(input("Se for somar digite 1,se for subitrair 2, multplicar 3 e dividir 4:"))

if operação == 1:
    somar = int(num1 + num2)
    print("Resultado = %d" % somar)
elif operação == 2:
    subtrair = int(num1 - num2)
    print("Resultado = %d" % subtrair)
elif operação == 3:
    multiplicar = int(num1 * num2)
    print("Resultado = %d" % multiplicar)
elif operação == 4:
    dividir = float(num1 / num2)
    print("Resultado = %f" % dividir)
else:
    print(" Operação invalida digite opções de 1 a 4!")
