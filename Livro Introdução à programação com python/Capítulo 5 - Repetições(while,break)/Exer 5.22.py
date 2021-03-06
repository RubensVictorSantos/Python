print("Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): \n"
"adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação \n"
"escolhida. Repita até que a opção saída seja escolhida.\n")

sair = ''
while True:

    tabuada = 1

    operação = int(input(
    "                      -------------------------------------\n"
    "                      |                 MENU              |\n"
    "                      -------------------------------------\n"
    "                      |P/ adição         aperte      1    |\n"
    "                      |P/ subtração      aperte      2    |\n"
    "                      |P/ divisão        aperte      3    |\n"
    "                      |P/ multiplicação  aperte      4    |\n"
    "                      |P/ sair           aperte      5    |\n"
    "                      -------------------------------------\n"
                         "\n Escolha uma das operações: "))

    if operação == 5:
        print("\n            ||     |||      ||      ||        ||     !!  !!  !!\n"
              "            |||   ||||      ||      |||      |||     !!  !!  !!\n"
              "            ||||||| ||      ||      ||||    ||||     !!  !!  !!\n"
              "            ||      ||      ||      || ||  || ||     !!  !!  !!\n"
              "            ||              ||      ||  ||||  ||     !!  !!  !!\n"
              "            |||||           ||      ||   ||   ||     !!  !!  !!\n"
              "            ||              ||      ||        ||     !!  !!  !!\n"
              "            ||              ||      ||        ||               \n"
              "            ||              ||      ||        ||     !!  !!  !!\n")
        break

    num = int(input("\n Dígite um numero: "))
    while tabuada <= 10:

        if operação == 1:
            resul = num + tabuada
            print (" %d + %d = %d " % (num,tabuada,resul))
        elif operação == 2:
            resul = num - tabuada
            print (" %d - %d = %d " % (num,tabuada,resul))
        elif operação == 3:
            resul = num / tabuada
            print (" %d / %d = %.1f " % (num,tabuada,resul))
        elif operação == 4:
            resul = num * tabuada
            print (" %d * %d = %d " % (num,tabuada,resul))
        else:
            print (" Essa operação não existe!!! ")


        tabuada += 1
