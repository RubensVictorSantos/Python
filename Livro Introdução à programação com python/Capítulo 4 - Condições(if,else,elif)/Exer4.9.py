print("Exercício 4.9 Escreva um programa para aprovar o empréstico bancário para"
" compra de uma casa. O programa deve perguntar o valor da casa a comprar, o "
"salário e a quantidade de anos a pagar. O valor da prestação mensal não pode"
" ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor"
" da casa a comprar dividido pelo pelo número de meses a pagar. \n")

imovel = float(input("Digite o valor do imóvel:"))
salario = float(input("Digite o valor do seu sálario:"))
anos = int(input("Digite a quantidade de anos a pagar:"))
prestação = float(imovel/(anos*12))
porcentagem = float(prestação/salario*100)
print("Seriam %6.2f mensalmente, isso corresponde a %d porcento do seu salário. " % (prestação,porcentagem))
if porcentagem <= 30:
    print("Imprestimo permitido")
else:
    print("Não foi possivel obter imprestimo")
