print("Exercício 5.27 Escreva um programa que verifique se\n"
"um número é palíndromo se continua o mesmo caso seus dígitos\n"
"sejam invertidos. Exemplo: 454, 10501.")

num = input('Digite um número: ')
try:
    val = int(num)
    if num == str(num) [::-1]:
        print ('Esse número é palíndromo')
    else:
        print('Esse número não é palíndromo')

except ValueError:
        print('Esse número não é valido, tente novamente!')

