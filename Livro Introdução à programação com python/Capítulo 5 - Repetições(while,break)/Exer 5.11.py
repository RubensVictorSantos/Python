print("Exercício 5.11 Escreva um programa que pergunte o \n"
"depósito inicial e a taxa de juros de uma poupança. Exiba\n"
"os valores mês a mês para os 24 primeiros meses. Escreva o\n"
"total ganho com juros no período.\n")

cont = 1
dep = float(input("Digite o deposito inicial: "))
taxa = float(input("Digite a taxa de juros: "))
nova_taxa = 0
total_final = 0

while cont <= 24:

    nova_taxa = ((taxa/100)*dep)
    dep = dep + nova_taxa

    print(" %d° mês: R$ %.02f " % (cont,dep))
    cont = cont + 1

total_final = dep

print("\n Total final: R$ %.02f " % total_final)
