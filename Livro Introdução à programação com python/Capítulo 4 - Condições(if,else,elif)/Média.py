print ("Média do aluno")
nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))
soma = ((nota1 + nota2 + nota3 )/ 3)
print ("Média do aluno = %d" % soma)
if soma >= 7:
    print("Aprovado!")
elif soma >= 6:
    print ("Recuperação")
else:
    print("Reprovado")
