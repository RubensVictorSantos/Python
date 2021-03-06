print("Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo"
" fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o"
"tipo de instalação: R para residência, I para industria e C para comércio."
" Calcule o preço a pagar de acordo com a tabela a seguir. \n ")

kWh = int(input("Digite a quantidade de kWh:"))
Instalação = input("Digite o tipo de instalação(1 para residencial)(2 para comercial)(3 para industrial):")
if Instalação == 1:
    if kWh <= 500:
        preço = int(kWh*0.40)
    else:
        preço = int(kWh*0.65)
else:
    if Instalação == 2:
        if kWh <= 1000:
            preço = int(kWh*0.55)
        else:
            preço = int(kWh*0.60)
    else:
        if Instalação == 3:
            if kWh <= 5000:
                preço = int(kWh*0.55)
            else:
                preço = int(kWh*0.60)
        else:
            print("Preço = %d"% preço)
