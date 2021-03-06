print("Exercício 3.13 Escreva um programa que corverta uma temperatura digitada"
" em °C em °F. A fórmula para essa converção é F = (((9*c)/5)+35). \n ")

celsius = int(input("Digite a temperatura em celsius:"))
fahrenheit = int(((9*celsius)/5)+32)
print("Temperatura em Fahrenheit = %d" % fahrenheit)
