print(" Exercício 7.5 Escreva um programa que leia duas string\n"
"e gere uma terceira, na qual os caracteres da segunda foram\n"
"retirados da primeira")

str1 = input("Digite: ")
str2 = input("Digite: ")
str3=""
for e in str1:
    if e not in str2:
        str3 += e
print( str3)
