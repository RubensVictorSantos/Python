print("Exercício 6.6 Modifique o programa para trabalhar com \n"
"duas filas. Para facilitar seu trabalho, considere o comando\n"
"A para atendimento da fila1; e B, para atendimento da fila2.\n"
"O mesmo para a chegada de clientes: F para fila1; e G, para fila2.\n")

últimof1 = 10
últimof2 = 10
fila1 = list(range(1,últimof1+1))
fila2 = list(range(1,últimof2+1))
c = 0
x = 0
atendimentof1 = 0
atendimentof2 = 0

while True:
    print("\n Existem %d clientes na fila1"% len(fila1))
    print(" Fila1 atual:", fila1)
    print("\n Existem %d clientes na fila2"% len(fila2))
    print(" Fila2 atual:", fila2)
    print("\n Digite F para adicionar um cliente ao fim da fila1,\n"
         " ou A para realizar o atendimento da fila1. S para sair.\n"
         " Digite G par aadicionar um cliente ao fim da fila2,\n"
         " ou B para realizar o atendimento da fila2. S para sair.\n")

    operação = input("\n Operação (F,A,G,B e S): ")
    while c < len(operação):
        x = (operação[c])
        if x == "A":
            if (len(fila1))>0:
                atendimentof1 = fila1.pop(0)
            else:
                print("\n Fila vazia! Ninguém para atender.")
        elif x == "B":
            if (len(fila2))>0:
                atendimentof2 = fila2.pop(0)
            else:
                print("\n Fila vazia! Ninguém para atender.")
        elif x == "F":
                últimof1+=1 #Incrementa o ticket de novo cliente
                fila1.append(últimof1)
        elif x == "G":
                últimof2+=1 #Incrementa o ticket de novo cliente
                fila2.append(últimof2)
        else:
            print("\n Operação invalida! Digite apenas F, G, B, A ou S!")
        c+=1
    print("\n Cliente %d atendido da fila1"% atendimentof1)
    print(" Cliente %d atendido da fila2"% atendimentof2)
    if x == "S":
        print("\n Existem %d clientes na fila"% len(fila1))
        print(" Fila atual:", fila1)
        print("\n Existem %d clientes na fila"% len(fila2))
        print(" Fila atual:", fila2)
        break
    x = 0
    c = 0
