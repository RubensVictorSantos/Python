print ('''EXERCÍCIO 3.4 Escreva um a expressão para determinar se uma pessoa deve ou não pagar imposto.
       Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00''')
str_salario = input ("Digite o salário:")
salario = int(str_salario)

if salario >=  120000 :
    print("\nVocê deve pagar deu imposto")
else:
    print("\nVocê não precisa pagar imposto")
