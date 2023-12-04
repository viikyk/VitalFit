# IMPORTS
import time
import random

# LISTAS/DICIONÁRIOS
produtos = []
lista_desejos = []
historico_compras = []
estoque = []

def menu_mod2():
  print('''Escolha uma opção:
  1 - Cadastrar Produto
  2 - Perfil de Compra do Aluno
  3 - Promoções Personalizadas
  4 - Lista de Desejos
  5 - Avisos de Novos Produtos
  6 - Sistema de Pagamento
  7 - Acompanhamento de Entregas
  8 - Programa de Fidelidade
  9 - Avaliação de Produtos
  10 - Gestão de Estoque
  11 - SAIR/VOLTAR''')


def cadastro_produto(): # roupas e acessórios
  tamanhos_dispiniveis = ['PP', 'P', 'M', 'G', 'GG', 'XG', 'XGG', 'UNICO']
  produto = input('Produto: ')
  id_produto = int(input('ID: '))
  tamanho = input('Tamanho: ').upper()
  while tamanho != tamanhos_dispiniveis:
    tamanho = input('TAMANHO INVÁLIDO! Digite novamente: ').upper()
    if tamanho == tamanhos_dispiniveis:
      continue
  descricao = input('Descrição: ')
  preco = float(input('Preço: '))
  quantidade = int(input('Quantidade: '))
  imagem = input('Digite o caminho da imagem: ')
  # ARQUVO
  with open('produtos.txt', 'a') as arquivo:
    arquivo.write(f'{produto}, {id_produto}, {tamanho}, {descricao}, {preco}, {quantidade}, {imagem}')
    print(arquivo)
  try:
    with open('produtos.txt', 'r') as arquivo:
      arquivo.read()
      print(arquivo)
  except FileNotFoundError as erro:
    print(f'ERRO: {erro}! Arquivo não encontrado.')
  # GRAVANDO NA LISTA/DICIONÁRIO - GRAVANDO NO PRODUTO?
  produtos.append({'Produto': produto, 'ID': id_produto, 'Tamanho': tamanho, 'Descrição': descricao, 'Preço': preco, 'Quantidade': quantidade, 'Imagem': imagem})
  print(produtos)
  # GRAVANDO NO ESTOQUE
  estoque.append({'Produto': produto, 'ID': id_produto, 'Tamanho': tamanho, 'Quantidade': quantidade, 'Imagem': imagem})

def perfil_compra():
  print(' ..:: Bem vindo(a) ao seu portal de preferências! ::..')
  for historico in historico_compras:
    print(historico)
  cliente = input('Cliente: ')
  pref_estilo = input('Sua preferência de estilo? ')
  pref_tamanho = input('Sua preferência de tamanho: ').upper().split()
  pref_cor = input('Sua preferência de cor: ')
  historico_compras.append({'Cliente': cliente, 'Preferência de estilo': pref_estilo, 'Preferência de tamanho': pref_tamanho, 'Preferência de cor': pref_cor})
  

def promocoes():
  # se um produto aparecer mais de uma vez no historico de compra ou na preferencia, realizar uma promoção
  promocoes = []
  print(' ..:: CANAL EXCLUSIVO DE PROMOÇÕES ::.. ')
  for prod in historico_compras:
    if historico_compras.count(prod) > 1:
      print(f'Promoção para o produto {prod}! Aproveite!')
      promocoes.append(prod)
  promocao = input('Deseja comprar o produto da promoção? ')
  while promocao == 'Ss' or promocao == 'SIM' or promocao == 'Sim' or promocao == 'sim':
    print(f'Produto adicionado ao carrinho! Siga os próximos passos para realizar a compra.')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade: '))
    if produto and id_produto in promocoes:
      print(f'COMPRA REALIZADA COM SUCESSO!')
    historico_compras.append({'Produto': produto, 'ID': id_produto, 'Preço': preco, 'Quantidade': quantidade})
    if promocao == 'Nn' or promocao == 'NAO' or promocao == 'Nao' or promocao == 'nao':
      print('O produto foi adicionado a sua lista de desejos.')
      lista_desejos.append(produto)
      break
    

def lista_desejo():
  print(' ..:: Bem vindo(a) a sua lista de desejos! ::.. ')
  print()
  desejo = input('Deseja adicionar algum produto na sua lista de desejos? ')
  if desejo == 'Ss' or desejo == 'SIM' or desejo == 'Sim' or desejo == 'sim':
    id_produto = int(input('Digite o ID do produto: '))
    if id_produto in produtos:
      print(produtos[id_produto])
      lista_desejos.append({'ID': id_produto})
      print('PRODUTO ADICONADO À LISTA DE DESEJOS!')
  for p in historico_compras: 
    id_produto = p
    if historico_compras.count(p) > 1:
      print('Verifique o CANAL EXCLUSIVO DE PROMOÇÕES! Seu produto pode está em promoção!')
  

def novos_produtos():
  for novo_p in historico_compras:
    pref_estilo = novo_p
    print(novo_p)
    print('Existem produtos semelhantes a sua preferencia de estilo! Vem conferir!')
  # perguntar se quer receber avisos por email ou pelo aplicativo
  print('''Por onde deseja receber avisos de novos produtos/coleções?
  1. Email
  2. Aplicativo''')
  op = int(input('Opção: '))
  if op == 1:
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    end_email = input('Digite o endereço de email: ')
    dias = input('Quais os dias que deseja receber avisos sobre os produtos? ')
    if dias in dias_semana:
      print('Dias registrado com sucesso!')
    print(f'Você receberá os avisos por email no endereço {end_email} nos dias {dias}!')
    # pedir endereço de email e perguntar os dias que deseja receber avisos
  elif op == 2:
    notificacao = input('Deseja ativar as notificações para receber avisos sobre os produtos? ')
    while notificacao == 'Ss' or notificacao == 'SIM' or notificacao == 'Sim' or notificacao == 'sim':
      print('Notificações ativadas com sucesso!')
      if notificacao == 'Nn':
        break
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

def sistema_pagamento():
  status_pagamento = ['Pendente', 'Aguardando pagamento', 'Concluido']
  print('''Qual forma de pagamento deseja utilizar?
  1. Dinheiro/Boleto
  2. Cartão''')
  opc = int(input('Opção: '))
  if opc == 1:
    print('Método escolhido: Boleto')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Preço do produto: '))
    status_pagamento == 'Aguardando pagamento'
    print('Seu boleto foi gerado! Estaremos aguadando seu pagamento.')
    ponto_fidelidade = 15
    historico_compras.append({'Produto': produto, 'ID': id_produto, 'Ponto de Fidelidade': ponto_fidelidade})
  elif opc == 2:
    print('Método escolhido: Cartão')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Preço do produto: '))
    titular_cartao = input('Titular do cartão: ')
    numero_cartao = int(input('Número do cartão: '))
    banco = input('Seu banco: ')
    print('CARTÃO REGISTRADO! Estamos processando seu pagamento. Só um momento')
    time.sleep(1.5)
    status_pagamento == 'Concluido'
    print('Sua compra foi aprovada! Pagamento processado com sucesso!')
    ponto_fidelidade = 30
    historico_compras.append({'Produto': produto, 'ID': id_produto, 'Ponto de Fidelidade': ponto_fidelidade})
  else:
    print('MÉTODO DE PAGAMENTO INVÁLIDO! Tente novamente mais tarde.')

def acompanhamento_entregas():
  possiveis_status = ["Em processamento", "Em trânsito", "Entregue"]
  codigo_rastreio = int(input('Digite o código de rastreio da sua entrega: '))
  print('Só um momento...')
  novo_status = random.choice(possiveis_status)
  status_atual = novo_status
  # informações em tempo real do status da entrega, podendo acompanhar o progresso da entrega
  while status_atual != "Entregue":
    time.sleep(2) 
    print(f'O status atual da sua entrega é {status_atual}')
    if status_atual == 'Entregue':
      print('Produto entregue com sucesso!')
      break

def programa_fidelidade():
  pontos = []
  print('''Escolha uma opção:
  1 - Realizar compra
  2 - Consultar pontos
  3 - Trocar pontos''')
  opc_pontos = int(input('Opção: '))
  if opc_pontos == 1:
    cliente = input('Cliente: ')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade: '))
    pontos_ganhos = int(preco / 10) # Exemplo: 1 ponto para cada R$10 gastos
    pontos.append({'Cliente': cliente, 'Produto': produto, 'ID': id_produto, 'Preço': preco, 'Quantidade': quantidade, 'Pontos ganhos': pontos_ganhos})
    if cliente in pontos:
        pontos[cliente] += pontos_ganhos
    else:
        pontos[cliente] = pontos_ganhos
    print(f'Compra realizada por {cliente}. Pontos acumulados: {pontos_ganhos}.')
    print()
  elif opc_pontos == 2:
    if cliente in pontos:
      return pontos[cliente]
    else:
      return 0
  elif opc_pontos == 3:
    if cliente in pontos and pontos[cliente] >= pontos_ganhos:
      pontos[cliente] -= pontos_ganhos
      print(f'{cliente} trocou {pontos_ganhos} pontos por um desconto ou brinde exclusivo.')
    else:
      print(f'{cliente} não possui pontos suficientes para realizar a troca.')
      print()
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

def avalia_produto():
  avaliacao = input('Qual produto deseja avaliar? ')
  nota = int(input('Atribua uma nota para esse produto: '))
  comentario = input('Dê sua opnião sobre o produto: ')
  melhoria = input('O que você acha que pode ser melhorado? ')
  print(f'Produto avaliado: {avaliacao}, Nota: {nota}, Comentário: {comentario}, Melhoria: {melhoria}')
  print('Agradecemos o seu feedback! Sua opinião é de suma importância para a melhora da nossa rede.')

def gestao_estoque():
  quantidade_inicial = 1
  print('''Escolha uma opção:
  1 - Adicionar produto
  2 - Atualizar o estoque
  3 - Realizar venda
  4 - Monitorar o estoque''')
  opc_estoque = int(input('Opção: '))
  if opc_estoque == 1:
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    estoque.append({'Produto': produto, 'ID': id_produto, 'Quantidade': quantidade})
    if produto not in estoque:
      estoque[produto] = quantidade_inicial
      print(f'Produto {produto} adicionado ao estoque com quantidade inicial de {quantidade_inicial}.')
    else:
      print(f"Produto '{produto}' já existe no estoque.")
    print()
  elif opc_estoque == 2:
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    if produto in estoque:
      estoque[produto] += quantidade
      print(f'Estoque de {produto} atualizado para {estoque[produto]} unidades.')
    else:
      print(f'Produto {produto} não encontrado no estoque.')
      print()
  elif opc_estoque == 3:
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    if produto in estoque and estoque[produto] >= quantidade:
      estoque[produto] -= quantidade
      print(f'Venda de {quantidade} unidades de {produto} realizada com sucesso. Estoque atual: {estoque[produto]} unidades.')
    else:
      print(f'Venda de {quantidade} unidades de {produto} não pode ser realizada. Estoque insuficiente.')
    print()
  elif opc_estoque == 4:
    for e in estoque:
      print(' ..:: MONITORAMENTO DO ESTOQUE ::..')
      produto, quantidade = e.items()
      print(f'Produto: {produto} - Quantidade: {quantidade}')
      print(e)
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')
