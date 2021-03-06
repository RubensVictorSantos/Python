print("Exercício 5.21 Rescreva o programa da listagem 5.14 de forma a continuar \n"
"executando até que o valor digitado seja 0. Utilize repetição aninhadas")

valor = 0
células = 0
atual = 50
apagar = valor
while True:

    valor = int(input("Dígite o valor a pagar: "))

    if atual <= apagar:
        apagar -= atual
        células += 1
    else:
        print ("%d célula(s) de R$%d" % (células, atual))
        if apagar == 0:
            valor = int(input("Dígite o valor a pagar: "))
            

        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        células = 0
