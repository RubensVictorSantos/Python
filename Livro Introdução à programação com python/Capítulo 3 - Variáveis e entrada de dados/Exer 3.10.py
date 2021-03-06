print ("Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele"
" deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor "
"do aumento e do novo salário. \n ")


Salario = float(input("Digite o salário:"))
Aumento = float(input("Digite a porcentagem a ser acrescentado:"))
Valor_aumento = int(((Aumento / Salario) * 100))
Novo_salario = (Salario + ((Aumento / Salario) * 100))
print ("Valor do aumento = R$%5.2f" % Valor_aumento)
print ("Novo salário = R$%5.2f" % Novo_salario)
