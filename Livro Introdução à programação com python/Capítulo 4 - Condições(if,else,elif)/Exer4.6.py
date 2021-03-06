print("Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro"
" deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km"
" para viagens de até de 200 km, e R$ 0,45 para viagens mais longas. \n")

km = float(input("Qunatos km você pretende percorrer:"))
if km<=200:
    passagem = float(km * 0.50)
    print("Passagem = R$%5.2F"% passagem)
else:
    passagem = float(km * 0.45)
    print("Passagem = R$%5.2F"% passagem)
