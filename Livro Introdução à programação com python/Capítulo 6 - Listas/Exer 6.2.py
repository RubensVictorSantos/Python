print("Exercício 6.2 Faça um programa que leia duas listas e que \n"
" gere uma terceira com os elementos das duas primeiras.\n")

l=[1,2,3]
v=[4,5,6]
r=[]

r.extend(l+v)
print ("lista r: ", r)
'''extend é um método que ao contrario do append só adiciona os elementos
de uma lista a outra'''
