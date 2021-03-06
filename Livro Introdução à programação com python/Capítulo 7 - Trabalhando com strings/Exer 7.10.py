print(" Exercício 7.10 Escreva um jogo da velha para dois jogadores.\n"
" O jogo deve perguntar onde você que jogar e alternar entre os jogadores.\n"
" A cada jogada, verifique se a posição está livre. Verifique também quando\n"
"um jogador venceu a partida. Um jogo da velha pode ser visto como uma lista\n"
"de 3 elementos, onde cada elemento é outra lista, também com três elementos.\n"
'''
Exemplo do jogo:

 X | 0 |
---+---+---
   | X | X
---+---+---
   |   | 0
'''
" Onde cada posição pode ser vista como um número. Confira abaixo um exemplo\n"
"das posições mapeadas para a mesma posição de seu teclado numérico.\n")
'''
 7 | 8 | 9
---+---+---
 4 | 5 | 6
---+---+---
 1 | 2 | 3
'''

rows3 = [7,8,9]
rows2 = [4,5,6]
rows1 = [1,2,3]
rows = [rows1,rows2,rows3]
for x in range(30):
    print()
print("   Sua vez jogador1!\n"
      "\n"
      "       POSIÇÕES \n"
      "      7 | 8 | 9 \n"
      "     ---+---+---\n"
      "      4 | 5 | 6 \n"
      "     ---+---+---\n"
      "      1 | 2 | 3 \n")
posição = int(input("Em qual posição vc deseja jogar?: "))

for e in rows:
    e.find(posição)
