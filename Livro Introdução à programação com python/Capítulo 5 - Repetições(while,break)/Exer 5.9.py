print("Execício 5.9 Escreva um programa que leia dois números. Imprima a divisão\n"
" inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas\n"
" os operadores de soma e subtração para calcular o resultado. Lembre-se de que\n"
" podemos entender o quociente da divsão de dois números como a quantidade de \n"
"vezes que podemos retirar o divisor do dividendo. Logo, 20/4 = 5, uma vez que\n"
" podemos subtrair 4 cinco vezes de 20. \n")

num1 = int(input(" Digite o dividendo: "))#dez
num2 = int(input(" Digite o divisor: "))#2

resul = 0#5
resto = 0

while num1 < num2:
    print(" \nDividendo não pode ser maior que o divisor: ")
    num1 = int(input(" \nDigite o dividendo: "))#dez
    num2 = int(input(" Digite o divisor: "))#2

while num1 > 0:

    num1 = num1 - num2

    resul = resul + 1

resto = num1
print(" Quociente = %.0f \n Resto = %d " % ( resul, resto))
