print("Exercício 6.5 Altere o programa da listagem 6.21\n"
"de forma a poder trabalhar com vários comandos digitados\n"
"de uma só vez. Atualmente, apenas um comando pode ser\n"
"inserido por vez. Altere-o de forma a considerar operação\n"
"como uma string."

"Exemplo: FFFAAAS significaria três chegadas de novos \n"
"clientes, três atendimentos e, finalmente, a saída do programa.\n")

último = 10
fila = list(range(1,último+1))
c = 0 #Contador
x = 0
#atendimento = 0

while True:
    print("\n Existem %d clientes na fila"% len(fila))
    print(" Fila atual:", fila)
    print(" Digite F para adicionar um cliente ao fim da fila,\n ou A para realizar o atendimento. S para sair.")
    operacao = input("\n Operação (F,A ou S): ")
    while c < len(operacao):
        x = (operacao[c])
        if x == "A":
            if (len(fila))>0:
                atendimento = fila.pop(0)
            else:
                print("\n Fila vazia! Ninguém para atender.")
        elif x == "F":
                último+=1 #Incrementa o ticket de novo cliente
                fila.append(último)
        else:
            print("\n Operação invalida! Digite apenas F, A ou S!")
        c+=1
    print("\n Cliente %d atendido"% atendimento)
    if x == "S":
        print("\n Existem %d clientes na fila"% len(fila))
        print(" Fila atual:", fila)
        break
    x = 0
    c = 0
