from prettytable import PrettyTable #de https://pypi.org/project/prettytable/
 
def imprimir_voos(agenda):
  id_voo = -1
  preco_total = 0
  tabela = PrettyTable(['Pessoa', 'Origem', 'Destino', 'Hora de Saída', 'Hora de Chegada', 'Valor'])
  for i in range(len(agenda) // 2):
    nome = pessoas[i][0] #pega o nome do viajante
    origem = pessoas[i][1] #pega o aeroporto de origem
    id_voo += 1 #auxiliar para percorrer a lista da agenda
    ida = voos[(origem, destino)][agenda[id_voo]] #indice da agenda dos voos
    preco_total += ida[2]
    volta = voos[(destino, origem)][agenda[id_voo]]
    preco_total += volta[2]
    valor_pessoal = ida[2] + volta[2]
 
 
    #acrescenta a linha na tabela...:
    tabela.add_row([nome, origem, destino, ida[0], ida[1], ida[2]])
    tabela.add_row([nome, destino, origem, volta[0], volta[1], volta[2]])
    tabela.add_row([' ', ' ', ' ', ' ', 'Total deste passageiro:', valor_pessoal])
    tabela.add_row(['-', '-', '-', '-', '-', '-'])
 
  print(tabela)
  print(f'Valor total gasto: {preco_total}')