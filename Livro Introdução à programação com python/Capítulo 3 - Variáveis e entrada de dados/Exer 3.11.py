print ("Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria"
" e o percentual de desconto. Exiba o valor do desconto e o preço a pagar. \n")


P_mercadoria = float(input("Digite o preço da mercadoria:"))
Percentual = float(input("Digite o percentual de desconto:"))
Valor_desconto = ((Percentual / P_mercadoria) * 100)
Valor_descontado = (P_mercadoria - Valor_desconto)
print ("Desconto = R$%5.2f" % Valor_desconto)
print ("Preço da mercadoria com desconto = R$%5.2f" % Valor_descontado)
