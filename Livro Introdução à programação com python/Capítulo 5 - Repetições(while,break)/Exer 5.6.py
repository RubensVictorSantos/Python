print("Exercício 5.6 Altere o programa anterior para exibir os resultados no "
"mesmo de uma tabuada: 2x1 = 2, 2x2 = 4,... \n")

n = int(input("Tabuada de:"))
x = 0
while x <= 10:
    print(n,"X",x,"=",n*x)
    x=x+1
