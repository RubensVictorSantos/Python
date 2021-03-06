print("Exercício 5.23 Escreva um programa que leia um número e verifique se \n"
"é ou não um número primo. Para fazer essa verificação, calcule o resto da \n"
"da divisão do número por 2 e depois por todos os números ímpares até o número\n"
"lido. Se o resto de uma dessas divisões for igual a zero, o número não é\n"
"primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é\n"
"par.\n")

num = int(input(" Digite um número: "))
x=0
n=list(range(1,num+1))
for e in n:
    if num%e == 0:
        x+=1
if x == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
