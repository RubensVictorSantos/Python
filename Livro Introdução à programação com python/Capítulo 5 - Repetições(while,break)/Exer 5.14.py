print("Execício 5.14 Escreva um programa que leia números inteiros do teclado. \n"
"O programa deve ler números até que o usuário digite 0 (zero). No final da \n"
"execução, exiba a quantidade de números digitados, assim como a soma e a média \n"
"aritimética. \n")

soma = 0
cont = 1

while True:

    num = int(input(" Digite %d° número: " % cont))
    if num == 0:

        break

    soma = soma + num
    cont += 1
Qtd = cont
media = soma / Qtd
print("\n Soma: %d \n Quantidade de números digitados: %d \n Média: %f " % (soma,Qtd,media))
