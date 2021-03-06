#Test
'''for t in range(3,33,3):
    print(t, end="")
print()'''
"""L=[5,9,13]
x=0
for e in L:
    print("[%d] %d"% (x,e))
    x+=1
print()
x=0
for x,e in enumerate(L):
    print("[%d] %d" %(x,e))
print()
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
"""
'''
Lista_de_palavras = {"r":"carro",
                     "u":"louza",
                     "b":"avião",
                     "e":"barco",
                     "n":"cor",
                     "s":"mão"}
numero = input("Digite um número: ")
#índice = (numero*776)% len(Lista_de_palavras)

palavra = Lista_de_palavras[numero]
print(palavra)'''
'''
lapis = ["coloridos","neutros"]
caneta = ["coloridas","padrão"]
borracha = ["grande","media","pequena"]
material = [lapis,caneta,borracha]

for e in material:
    print(e)
    for e1 in e:
        print(e1)'''
'''def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None
L=[10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))'''
'''def f(n):
    if n<=1:
        return n
    else:
        return f(n-1)+f(n-2)
print(f(3))'''
'''myfunc = lambda i: i*2
print(myfunc(4))'''
'''def faixa_int(per,mín,máx):
    while True:
        v=int(len(per))
        if v<mín or v>máx:
            print('Valor inválido. Digite um valor entre %d e %d'%(mín,máx))
        else:
            return v
        break
p = input("Digite sua senha:")
faixa_int(p,5,8)'''
'''def soma(a,b, imp=False):
    s = a+b
    if imp:
        print(s)
    return s

print(soma(2,3))
print(soma(3,4,True))
print(soma(5,8,False))'''
'''def ret(lar,alt,carac="*"):
    linha = carac * lar
    for i in range(alt):
        print(linha)
print(ret(100,4))'''
def soma(a,b):
    print(a+b)
L=[2,3]
soma(*L)
