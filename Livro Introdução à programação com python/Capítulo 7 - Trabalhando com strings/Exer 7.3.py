print(" Exercício 7.2 Escreva um programa que leia duas strings\n"
" e gere uma terceira apenas com os caracteres que aparecem em uma delas.\n"
"\n 1 str: CTA\n"
" 2 str: ABC\n"
" Resultado: BT\n"
" A ordem dos caracteres da terceira string gerada não é importante.\n")

str1 = input(" Digite uma frase: ")
str2 = input(" Digite outra frase: ")
str3 = ''
for e in str2:
    if str1.find(e) == -1:
        str3+=e
        
for e in str1:
    if str2.find(e) == -1:
        str3+=e
print("\n Resultado:",str3)
