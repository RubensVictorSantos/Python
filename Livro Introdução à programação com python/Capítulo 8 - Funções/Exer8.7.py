print('Exercício 8.7 Defina uma função recursiva que calcule o maior divisor comum\n'
'(M.D.C.)entre dois números a e b, onde a > b.\n')

def mdc(a = 0 ,b = 0):

    cont = 2

    while(a > 0):

        if(a%cont == 0):
            print(a ,"-", cont )
            a = a//cont
            if(a//cont == 0):
                break
        else:
            cont += 1
    return mdc(b)
mdc(20,24)
