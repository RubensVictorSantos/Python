print("Exercício 6.13 Alista de temperatura de Mons, na Bégica, foi armazenada\n"
"na lista T=[-10,-8,0,1,2,5,-2,-4]. Faça um programa que imprima a menor e a\n"
"temperatura, assim como a temperatura média.\n")
T=[-10,-8,0,1,2,5,-2,-4]
mínimo = T[0]
máximo = T[0]
soma = 0
for e in T:
    if e < mínimo:
        mínimo = e
    elif e > máximo:
        máximo = e
    soma = soma + e
média = soma / len(T)
print(" Mínima de %d\n Máxima de %d\n Temperatura média: %d"% (mínimo,máximo,média))
