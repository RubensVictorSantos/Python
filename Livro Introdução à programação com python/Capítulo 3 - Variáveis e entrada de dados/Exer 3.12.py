print("Execício 3.12 Escreva um programa que calcule o tempo de uma viagem de "
"carro. Pergunte a distância a percorrer e a velocidade média esperada para a "
"viagem. \n ")

distancia = int(input("Digite a distância:"))
velocidade = int(input("Digite a velocidade:"))
tempo = int(distancia/velocidade)
print("Tempo de viagem = %d Horas" % tempo)
