print("Exercício 5.13 Escreva um programa que pergunte o valor\n"
"inicial de uma dívida e juro mensal. Pergunte também o valor\n"
"mensal que será pago. Imprima o número de meses para que a \n"
"dívida seja paga, o total de juros pago. \n")

divida = float(input("Digite o valor da divida: "))
juros = int(input("Digite o valor do juros mensal: "))
valor = float(input("Digite o valor que você pretende pagar por mês "))

mes = 0

while divida > valor:
    divida -= valor
    divida += juros
    mes += 1
    totaljuros = juros + juros

print("Total de meses:",mes ,"\nTotal de juros:",totaljuros)
