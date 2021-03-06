print("Exercício 6.7 Faça um programa que leia uma expressão\n"
"com parênteses. Usando pilhas, verifique se os parênteses\n"
"foram abertos e fechados na ordem correta.\n")
lista1=[]
lista2=[]
paren = ""
x = 0
c = 0
while True:
    paren = input("Digite:")
    if (paren[0])==")":
        print("Erro")
    else:
        while c < len(paren):
            x = (paren[c])
            if x == "(":
                lista1.append(x)
            else:
                lista2.append(x)
            c+=1
        c=0
        if len(lista1)==len(lista2):
            print("OK")
        else:
            print("ERRO")
    lista1=[]
    lista2=[]
