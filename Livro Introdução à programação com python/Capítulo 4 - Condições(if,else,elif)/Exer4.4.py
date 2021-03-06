print("Exercício 4.4 Escreva um programa que pergunte o salário do funcionário"
" e calcule o valor do aumento. Para salário superior a R$ 1.250,00, calcule um"
" aumento de 10%. Para os inferiores ou iguais, de 15. \n")

salario = float(input("Dígite o salário: "))

if salario > 1250.00 :
    
    salario = float((1+0.10)*salario)
    print ("Reajuste de 10 porcento = R$%5.2F" % salario)
    
else:
    salario = float((1+0.15)*salario)
    print ("Reajuste de 15 porcento = R$%5.2F" % salario)
