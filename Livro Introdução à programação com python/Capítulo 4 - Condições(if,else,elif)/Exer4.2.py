print("Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de"
" um usuário. Caso ultrapasse 80 km/h, exiba uma mensegem dizendo que o usuário"
" foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima"
" de 80 km/h. \n")


velocidade = float(input("Digite a velocidade:"))
multa = int((velocidade - 80)*5)
if velocidade > 80:
    print("Você foi multado, no valor de R$ %5.2f" % multa)
else:
    print("Você não foi multado")
