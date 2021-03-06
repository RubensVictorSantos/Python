print("Exercício 6.17 Altere o programa da listagem 6.53 de forma\n"
"a solicitar ao usuário o produto e a quantidade vendida. Verifique\n"
"se o nome do produto digitado existe no dicionário, e só então\n"
"efetue a baixa em estoque.\n")

t=0
estoque={"tomate": [ 1000, 2.30],
         "alface": [  500, 0.45],
         "batata": [ 2001, 1.20],
         "feijão": [  100, 1.50] }
print("Tabela: ", estoque, end=" ")
while True:
    Dprod=input("\n Digite o produto: ")
    Dquant=int(input(" Digite a quantidade desejada: "))
    venda = [[Dprod, Dquant]]
    total=0
    print("\n Vendas:\n")
    for operação in venda:
        produto, quantidade = operação
        preço = estoque[produto][1]
        custo = preço*quantidade
        print("%12s: %3d x %6.2f = %6.2f"%(produto, quantidade, preço, custo))
        estoque[produto][0] -= quantidade
        total+=custo
    t+=total
    fim = input("\n Deseja finalizar(s/n): ")
    if fim == "s":
        break
print(" Custo total: %21.2f\n" % t)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
