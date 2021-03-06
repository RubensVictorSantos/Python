print(" Execício 7.1 Escreva um programa que leia suas strings\n"
" Verifique se a segunda ocorre dentro da primeira e imprima a\n"
" posição de ínicio.\n"
" 1 string:AABBEFAATT\n"
" 2 string: BE\n"
" Resultado: BE encontrado na posição 3 de AABBEFAATT\n")

str1 = input(" Digite uma frase: ")
str2 = input(" Procurar dentro da frase: ")

find = str1.find(str2)

print("\n Resultado: %s encontrado na posição %d de %s." % (str2,find,str1))
