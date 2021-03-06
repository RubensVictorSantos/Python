print("Exercício 6.12 Altere o programa da listagem 6.33 de forma a imprimir\n"
"o menor elemento da lista.\n")

L=[1,7,2,4]
mínimo = L[0]
for e in L:
    if e < mínimo:
        mínimo = e
print("Valor mínimo: ",mínimo)
