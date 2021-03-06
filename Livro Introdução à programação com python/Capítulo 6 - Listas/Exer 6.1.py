print("Exercício 6.1 Modifique o programa da listagem 6.6 para\n"
"ler 7 notas em vez de 5.\n")

notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 7 :# Essa estrutura vai pedir as notas

    notas[x] = float(input(" Nota %d: " % x))
    soma += notas[x]
    x += 1
x = 0
while x < 7 :

    print(" Nota %d: %6.2f" % (x, notas[x]))
    x += 1
print(notas)
print(" Média: %5.1f" % (soma/x))
