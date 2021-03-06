print("Exercício 5.5 Reescreva o programa anterior para \n"
"escrever os 10 primeiros múltiplos de 3. \n")

fim = int(input("Digite o último número:"))
x = 0
while x <= fim:
    if x%3 == 0:
        print(x)
    x=x+1
