print("Exercício 5.7 Modifique o programa anterior de forma \n"
"que o usuário também digite o início e o fim da tabuada, em\n"
"vez de começar com 1 e 10. \n")

n1 = int(input(" Tabuada de: "))
x = int(input(" \nNúmero inicial: "))
n2 = int(input(" Número final: "))
if x > n2:
    print("\n        Número inicial não pode ser menor que o final.")

while x <= n2:
    print(n1,"X",x,"=",n1*x)
    x = x+1
