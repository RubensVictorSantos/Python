print("Esse programa vai identificar os Ultimos dois numeros do RG")

C1 = int(input("digite o 1° digito ="))
C2 = int(input("digite o 2° digito ="))
C3 = int(input("digite o 3° digito ="))
C4 = int(input("digite o 4° digito ="))
C5 = int(input("digite o 5° digito ="))
C6 = int(input("digite o 6° digito ="))
C7 = int(input("digite o 7° digito ="))
C8 = int(input("digite o 8° digito ="))
C9 = int(input("digite o 9° digito ="))
#C10 = 0
#C11 = None
#res_C10 = None

res_C10 = int ((C1*1)+(C2*2)+(C3*3)+(C4*4)+(C5*5)+(C6*6)+(C7*7)+(C8*8)+(C9*9))
resto_div_C10 = int(res_C10 % 11)
res_C11 = int ((C1*9)+(C2*8)+(C3*7)+(C4*6)+(C5*5)+(C6*4)+(C7*3)+(C8*2)+(C9*1)  )
resto_div_C11 = int(res_C11 % 11)
print("decimo numero = %d e decimo primeiro = %d " % (resto_div_C10, resto_div_C11))

#res_C10 = ((C1*9)+(C2*8)+(C3*7)+(C4*6)+(C5*5)+(C6*4)+(C7*3)+(C8*2)+(C9*1)/11)

#div_res_C10 = (res_C10 % 11)
#str_div_res_C10 = str(div_res_C10)

#if div_res_C10 == 0 or 1:
#    C10 = (0)

#    print (C10)

#else:
#    C10 = (11 - (div_res_C10))

#    print (C10)
