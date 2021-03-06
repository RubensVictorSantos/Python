print("Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o\n "
"número digitado pelo usuário, mas, dessa vez, apenas os números ímpares. \n")

resp ="s"

while True:

    fim =int(input(" Digite o último numero:"))
    x = 0
    while x <= fim:
        if x%2 == 1:
            print( x )
        x=x+1

    resp = input(" Deseja continuar?(s/n) ")
    if (resp == "n" ):
        break
