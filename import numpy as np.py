import numpy as np



class VetorOrdenado:
     
  def __init__(vetor, capacidade):
    vetor.capacidade = capacidade
    vetor.ultima_posicao = -1
    vetor.valores = np.empty(vetor.capacidade, dtype=int)

  # O(n)
  def imprime(vetor):
    if vetor.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(vetor.ultima_posicao + 1):
        print('[{}] -> {}'.format(i, vetor.valores[i]))

  # O(n)
  def insere(vetor, valor):
    if vetor.ultima_posicao == vetor.capacidade - 1:
      print('Capacidade máxima atingida')
      return

    posicao = 0
    for i in range(vetor.ultima_posicao + 1):
      posicao = i
      if vetor.valores[i] > valor:
        break
      if i == vetor.ultima_posicao: # se já percorreu o vetor inteiro deve inserir na última posição
        posicao = i + 1

    x = vetor.ultima_posicao
    while x >= posicao:
      vetor.valores[x + 1] = vetor.valores[x]
      x -= 1 #x = x - 1

    vetor.valores[posicao] = valor
    vetor.ultima_posicao += 1

  # O(n)
  def pesquisa_linear(vetor, valor):
    for i in range(vetor.ultima_posicao + 1):
      if vetor.valores[i] > valor:
        return -1
      if vetor.valores[i] == valor:
        return i
      if i == vetor.ultima_posicao:
        return -1

  #dódigo corrigido pelo Dyego:
  def pesquisa_linear_while(vetor,valor):
    i = 0
    while(i < len(vetor.valores)) and (vetor.valores[i] < valor):
      i+=1
    return -1 if(i >= len(vetor.valores) or vetor.valores[i]) != valor else i


  def pesquisa_binaria(vetor, valor):
    limite_inferior = 0
    limite_superior = vetor.ultima_posicao

    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      #se encontrar na primeira tentativa:
      if vetor.valores[posicao_atual] == valor:
        return posicao_atual
      ##não encontrou...:
      elif limite_inferior > limite_superior:
        return -1
      #dividindo o vetor...:
      else:
        #limite inferior:
        if vetor.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual + 1
        #limite superior:
        else:
          limite_superior = posicao_atual - 1

  def excluir(vetor, valor):
    posicao = vetor.pesquisa_binaria(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, vetor.ultima_posicao):
        vetor.valores[i] = vetor.valores[i + 1];
      
      vetor.ultima_posicao -= 1