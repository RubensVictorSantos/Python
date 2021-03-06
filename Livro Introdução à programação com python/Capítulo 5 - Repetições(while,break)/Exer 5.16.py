print("Exercício 5.16 Execute o programa (Listagem 5.14) para os seguintes valores:\n"
" 501, 745, 384, 2, 7 e 1.\n")

valor = int(input("Dígite o valor a pagar: "))
células = 0
atual = 50
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        células += 1
    else:
        print ("%d célula(s) de R$%d" % (células, atual))
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        células = 0
