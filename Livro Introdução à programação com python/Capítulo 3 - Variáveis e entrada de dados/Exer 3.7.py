print ("Exercício 3.7 Faça um programa que peça dois números inteiros. Imprima "
"a soma desses dois números na tela \n ")

while True:
    num1 = float(input("\n Digite primeiro numero:"))
    num2 = float(input(" Digite segundo numero:"))
    soma = num1 + num2
    print ("\n Resultado: %d" % soma)

    resp = input("\n Deseja continuar?(s/n): ")
    if resp == "n":
        break
