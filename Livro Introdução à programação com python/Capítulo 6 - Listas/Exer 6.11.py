print("Exercício 6.11 Modifique o programa da listagem 6.15 usando for.\n"
"Explique por que nem todos os while podem ser transformados em for.\n")

L=[]
while True:
    n=int(input(" Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)

for x in L:
    print(x)
    x+=1
