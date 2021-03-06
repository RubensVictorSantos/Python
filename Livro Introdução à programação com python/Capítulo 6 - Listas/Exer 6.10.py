print("Exercício 6.8 Modifique o programa do exercício 6.9 de forma a\n"
"a pesquisar p e v em toda a lista e informando o usuário a posição onde\n"
"p e a posição onde v foram encontradas.")

L=[15,7,27,39,]
p=int(input("\n Digite o 1° valor a procurar: "))
v=int(input(" Digite o 2° valor a procurar: "))
x=0
while x <len(L):
    if L[x]==p:
        print("\n %d achado na posição %d " %(p,x))
    elif L[x]==v:
        print("\n %d achado na posição %d " %(v,x))
    x+=1
#print("\n %d não encontrado"%p)
