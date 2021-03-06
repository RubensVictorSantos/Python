print(' Exercício 8.11 Escreva uma função para validar uma variável\n'
'string. Essa função recebe como parâmetro a string, o número mínimo\n'
'e máximo de caracteres. Retorne verdadeiro se o tamanho da string\n'
'entre os valores de máximo e mínimo, e falso em caso contrário.\n')
def tam(ask,mín,máx):

    if int(len(ask))<mín or int(len(ask))>máx:
        return False
    
    else:
        return True

#-----------------------------------------------------------------------------
senha = input("Digite uma senha com no mínimo 5 caracteres e no máximo 8:")
tam(senha,5,8)
