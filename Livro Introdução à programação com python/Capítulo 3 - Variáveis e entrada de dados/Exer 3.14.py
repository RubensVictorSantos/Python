print("Exercício 3.14 Escreva um programa que pergunte a quantidade de km "
"percorridos por um carro alugado pelo usuário, assim como a quantidade de dias"
" pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro"
" custa R$ 60 por dia e R$ 0,15 por km rodado. \n")

km = int(input("Digite quantidade de km percorridos: "))
dias = int(input("Digite qunatidade de dias: "))
preço = int((60*dias)+(0.15*km))
print ("Valor a ser pago = R$%5.2f" % preço)
