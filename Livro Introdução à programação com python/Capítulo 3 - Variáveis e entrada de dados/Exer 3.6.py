print ("EXECÍCIO 3.6 Escreva uma expressão que será utilizada para decidir se um\n "
"aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem \n"
"ser maiores que 7. Considere que o aluno cursa apenas três matéria, e que a \n"
"nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e \n"
"matéria3. \n ")
resp = ""
while True:
    Matéria1 = int(input("\n Digite nota da 1ª matéria:"))
    Matéria2 = int(input(" Digite nota da 2ª matéria:"))
    Matéria3 = int(input(" Digite nota da 3ª matéria:"))
    Resultado = ((Matéria1 + Matéria2 + Matéria3 )/ 3)
    
    print ("\n Média do aluno =",Resultado)
    if Resultado >= 7:
        print("\n Aprovado!")
    else:
        print("\n Reprovado!")

    resp = input("\n Deseja continuar(s/n): ")
    if resp == "n":
        break
