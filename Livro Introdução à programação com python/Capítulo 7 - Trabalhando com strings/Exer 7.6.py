print(" Execício 7.6 Escreva um programa que leia três string.\n"
" Imprima o resultado da substituição na primeira, dos caracteres\n"
"da segunda pelos da terceira.")

str1 = input("str1: ")
str2 = input("str2: ")
str3 = input("str3: ")
x1 = ''
cont = 0

for e in str2:
    #str1.rfind(e)
    if str1.find(e) >= 0:
        x = str1.count(e)
    
print("Resultado: ",)
