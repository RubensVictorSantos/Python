print("Exercício 6.8 Modifique o primeiro exemplo (Listagem 6.23) de forma\n"
"a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: Observe\n"
"a condição de saída do while.\n")

L=[15,7,27,39]
p=int(input("\n Digite o valor a procurar: "))
x=0
while x <len(L):
    if L[x]==p:
        print("\n %d achado na posição %d " %(p,x))
        break
    x+=1
if x >= len(L):
    print("\n %d não encontrado"%p)
