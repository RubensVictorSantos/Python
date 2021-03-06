print("Exercício 5.19 Modifique o programa para também aceitar valores \n"
"decimais, ou seja, também contar moeda de 0,01, 0,02, 0,05, 0,10 e 0,50. \n")

valor = float(input("Dígite o valor a pagar: "))
células = 0
moedas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        células += 1
        moedas += 1
    else:
        print ("%d Célula(s) de R$ %5.2f \n%d Moeda(s) de %0d " % (células, atual,moedas,atual))
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1

        elif atual == 0.50:
            atual = 10
        elif atual == 0.10:
            atual = 5
        elif atual == 0.05:
            atual = 2
        elif atual == 0.02:
            atual = 1
        elif atual == 0.01:
            atual = 0.005

        células = 0
        moedas = 0
