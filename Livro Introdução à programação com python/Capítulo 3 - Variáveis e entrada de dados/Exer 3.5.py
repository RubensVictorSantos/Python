print ("EXERCÍCIO 3.5 Calcule o resultado da expressão A>B and C or D, utilizando"
" os valores da tabela a seguir. \n ")
print("     Tabela:\n"
"    ________________________ \n"
"   |A=1 |B=2|C=True |D=False|\n"
"   |A=10|B=3|C=False|D=False|\n"
"   |A=5 |B=1|C=True |D=True |\n"
"    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ \n")

A = int(input("Didite o valor de A:"))
B = int(input("Didite o valor de B:"))
C = input("Didite a condição de C:")
D = input("Didite a condição de D:")
print ("\nResultado: ", A > B and C or D)
