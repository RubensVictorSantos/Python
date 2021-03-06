print("Exercício 5.24 Modifique o programa anterior de forma a ler um número n.\n"
"Imprima os n primeiros números primos.\n")

num = int(input(" Digite um número: "))
cont = 1
if num == 2:
    print(" Esse número é primo")

    if num%2 != 0:

        impar = num

        while cont <= num:

            if num % impar == 0:
            cont += 1
