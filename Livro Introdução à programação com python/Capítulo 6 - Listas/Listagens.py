'''
print("Listagem 6.7 - Apresentação de números.\n")
num = [0,0,0,0,0]
x = 0
while x < 5 :

    num[x] = int(input(" Número %d: " % (x+1)))
    x += 1
while True:
    escolhido = int(input(" Que posição você quer imprimir (0 para sair): "))

    if escolhido == 0:
        break
    print(" Você escolheu o número: %d " % (num[escolhido-1]))
print()

print(" Listagem 6.34 - Cópia para outras listas.\n")
V=[9,8,7,12,0,13,21]
P=[]
I=[]
for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print(" Pares: ",P)
print(" Impares: ",I)
'''
'''
print("Listagem 6.35 - Controle da utilização de salas de um cinema.")
lugares_vagos=[10,2,1,3,0]
while True:
    sala=int(input("Sala (0 sai): "))
    if sala==0:
        print("Fim")
        break
    if sala>len(lugares_vagos)or sala<1:
        print("Sala inválida")
    elif lugares_vagos[sala-1]==0:
        print("Desculpe, sala lotada!")
    else:
        lugares=int(input(" Quantos lugares você deseja (%d vagos): " % lugares_vagos[sala-1]))
        if lugares>lugares_vagos[sala-1]:
            print(" Esse número de lugares não está disponível.")
        elif lugares<0:
            print("Número inválido")
        else:
            lugares_vagos[sala-1]-=lugares
            print(" %d lugares vendidos"% lugares)
print(" Utilizção das salas")
for x,l in enumerate(lugares_vagos):
    print(" Sala %d - %d lugar(es) vazio(s)"%(x+1,l))
'''
'''
print('Listagem 6.43 - Criação e impressão da lista de compras.')
compras=[]
while True:
    produto = input(' Produto: ')
    if produto == 'fim':
        break
    quantidade = int(input(" Quantidade: "))
    preço = float(input(" Preço: "))
    compras.append([produto, quantidade, preço])
soma = 0.0
for e in compras:
    print(" %20s x%5d %5.2f %6.2f" % (e[0],e[1],e[2],e[1]*e[2]))
    soma+= e[1] * e[2]
print(" Total: %7.2f" %soma)'''
'''print("Listagem 6.44 - Ordenação pelo método de bolhas")
#L=[7,4,2,12,8]
L=[1,2,3,4,5]
fim=5
while fim > 1:
    trocou=False
    x=0
    while x<(fim-1):
        if L[x]>L[x+1]:
            trocou=True
            temp=L[x]
            L[x]=L[x+1]
            L[x+1]=temp
        x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e)'''
    '''
print("Listagem 6.45 - Criação de um dicionário.")
Tabela={"Alface":0.45,
        "Batata":1.20,
        "Tomate":2.30,
        "Feijão":1.50}

print(Tabela["Alface"])
'''
