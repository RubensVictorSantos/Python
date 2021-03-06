print("Execício 5.12 Altere o programa anterior de forma a \n"
"perguntar também o valor depositado mensalmente. esse valor\n"
"será depositado no início de cada mês, e você deve\n"
"considerá-lo para o cálculo de juros do mês seguinte.\n")

cont = 1
taxa = float(input("Digite a taxa de juros: "))
nova_taxa = 0
total_final = 0

while cont <= 24:

    dep = float(input("Digite o deposito do %d mês: " % cont))
    nova_taxa = ((taxa/100)*dep)
    dep = dep + nova_taxa

    print(" %d° mês: R$ %.02f " % (cont,dep))
    cont = cont + 1

total_final = dep

print("\n Total final: R$ %.02f " % total_final)
