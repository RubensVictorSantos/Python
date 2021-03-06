print ("Exercícios 3.9 Escreva um programa que leia a quantidade de dias, horas,"
" minutos e segundos do usúario. Calcule o total em segundos. \n ")

Quant_dias = int(input("Digite quantidade de dias:"))
Quant_horas = int(input("Digite quantidade de horas:" ))
Quant_minutos = int(input("Digite quantidade de minutos:" ))
Quant_segundos = int(input("Digite quantidade de segundos:" ))
total = ((Quant_dias * 86400)+(Quant_horas * 3600)+(Quant_minutos * 60)+ Quant_segundos)
print ("Em segundos: %d" % total,"/s")
