print(" Exercício 7.2 Escreva um programa que leia duas strings\n"
" e gere uma terceira com os caracteres comuns às duas strings lidas.\n"
"\n 1 str: AAACTBF\n"
" 2 str: CBT\n"
" Resultado: CBT\n"
" A ordem dos caracteres da string gerada não é importante, mas deve\n"
" conter todas as letras comuns a ambas.\n")

str1 = input(" Digite uma frase: ").lower().strip()
str2 = input(" Digite outra frase: ").lower().strip()
str3 = ''
for e in str2:
    if str1.find(e) >= 0:
        str3+=e
print("\n Resultado: ",str3)
