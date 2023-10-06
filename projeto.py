from re import VERBOSE
import random

def exibir_matriz(matriz):
  print('   ', end='')
  for coluna in range(len(matriz[0])):
      print(coluna, end='  ')
  print()
  print('  +' + '---+' * len(matriz[0]))
  for linha in range(len(matriz)):
      print(linha, end=' | ')
      for coluna in range(len(matriz[linha])):
          print(matriz[linha][coluna], end=' | ')
      print()
      print('  +' + '---+' * len(matriz[linha]))

#Matriz vazia
linhas = 7
colunas = 7
matriz = []
for _ in range(linhas):
    linha = [' '] * colunas
    matriz.append(linha)


exibir_matriz(matriz)

jogador = 'O'
vencedor = None

while vencedor is None:
# JOGADA DO JODADOR(O Sr.(a))
  if jogador == 'O':
    linha_jogada= int(input("Digite o numero da linha que o Sr. quer jogar (0-6):  "))
    coluna_jogada= int(input("Digite o numero da coluna que o Sr. quer jogar (0-6): "))
    if matriz[linha_jogada][coluna_jogada] == ' ':
      matriz[linha_jogada][coluna_jogada] = jogador
      #VERIFICAR SE O JOGADOR FORMOU UM QUADRADO
      if linha_jogada > 0 and coluna_jogada > 0:
        if(matriz[linha_jogada][coluna_jogada-1 ] == matriz[linha_jogada-1][coluna_jogada-1] == matriz[linha_jogada-1][coluna_jogada] == matriz[linha_jogada][coluna_jogada]):
          vencedor = jogador
        if (matriz[linha_jogada][coluna_jogada-1] == matriz[linha_jogada][coluna_jogada] == matriz[linha_jogada-1][coluna_jogada] == matriz[linha_jogada-1][coluna_jogada-1]):
          vencedor = jogador
    else:
      print("Posição inválida!")

  else:
    #Sistema jogando aleatoriamente
    espacos_vazios = []
    for linha in range(len(matriz)):
      for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == ' ':
          espacos_vazios.append((linha, coluna))
    if espacos_vazios:
      linha, coluna = random.choice(espacos_vazios)
      matriz[linha][coluna] = 'X'
      #Verificação para ver se formou uma matriz 2x2
      for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
          if matriz[linha][coluna] == 'X':
            if linha > 0 and coluna > 0:
              if (matriz[linha][coluna-1] == matriz[linha-1][coluna-1] == matriz[linha-1][coluna] == matriz[linha][coluna]):
                vencedor = 'X'
                break
              if (matriz[linha][coluna-1] == matriz[linha][coluna] == matriz[linha-1][coluna] == matriz[linha-1][coluna-1]):
                vencedor = 'X'
                break
  jogador = 'X' if jogador == 'O' else 'O'

  #Mostrar o andamento da matriz
  exibir_matriz(matriz)

#Matriz Final (fim do jogo)
exibir_matriz(matriz)
print(f'O jogador, {vencedor}, perdeu')



