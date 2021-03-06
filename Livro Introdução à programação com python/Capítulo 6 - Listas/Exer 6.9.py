print("Exercício 6.8 Modifique o exemplo para pesquisar dois valores. Em\n"
"vez de apenas p, leia valor v que também será procurado. Na impressão,\n"
"indique qual dos dois valores foi achado primeiro.")

L=[15,7,27,39]
p=int(input("\n Digite o 1° valor a procurar: "))
v=int(input(" Digite o 2° valor a procurar: "))
achou=False
x=0
while x <len(L):
    
    if L[x]==p:
        achou=True
    elif L[x]==v:
        achou=True
    x+=1
if achou:
    print("\n %d achado na posição %d " %(p,x))
else:
    print("\n %d não encontrado"%p)
