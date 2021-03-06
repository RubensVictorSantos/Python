print ("Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora \n"
". Você deve solicitar ao usuário que digite o código do produto e a quantidade \n"
"comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto: \n"

"                              _______________\n"
"                              |Código| Preço|\n"
"                              |------+------|\n"
"                              |   1  | 0,50 |\n"
"                              |------+------|\n"
"                              |   2  | 1,00 |\n"
"                              |------+------|\n"
"                              |   3  | 4,00 |\n"
"                              |------+------|\n"
"                              |   5  | 7,00 |\n"
"                              |------+------|\n"
"                              |   9  | 8,00 |\n"
"                              ---------------\n"

"Seu programa deve exibir o total das compras depois que o usuário digitar \n"
"0. Qualquer outro código deve gerar a mensagem de erro Código inválido. \n")

end = ''
total = 0
#Qtd = 0

while True:

    codigo = int(input(" Dígite o código do produto: "))
    Qtd = int(input(" Dígite a quantidade comprada: "))

    if codigo == 1:
        preço = 0.50
    elif codigo == 2:
        preço = 1.00
    elif codigo == 3:
        preço = 4.00
    elif codigo == 5:
        preço = 7.00
    elif codigo == 9:
        preço = 8.00
    else:
        print("\n            Código inválido!!!")
        codigo = 0
        preço = 0
        break

    total = total + Qtd * preço

    end = input(" Deseja continuar?(s/n): ")
    if end == 'n':
        break

print ("\n Total das compras = R$%6.2f " % total)
