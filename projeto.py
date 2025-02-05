
import os # Importa uma biblioteca que verifica se o arquivo .txt existe.
import datetime # Importa uma biblioteca para trabalhar com datas ou horários.
import random # Importa uma biblioteca que pode gerar números aleatórios.

investidor = {  # Login do usuário/investidor.

    '123' : 'rafael',   
    '456' : 'rafael2'
}

menu = {    # Dicionário das opções do menu.
    1: 'Consultar Saldo',
    2: 'Consultar Extrato',
    3: 'Depositar',
    4: 'Sacar',                        
    5: 'Comprar Criptomoedas',
    6: 'Vender Criptomoedas',
    7: 'Atualizar Cotação',
    8: 'Sair'
}

criptomoedas = {    # Dicionário das criptomoedas.

    1: 'Bitcoin',
    2: 'Ethereum',
    3: 'Ripple',
    4: 'Sair'

}

taxa_compra_criptos = { # Dicionário das taxas de compra das criptomoedas.

    'Bitcoin' : 0.02,
    'Ethereum' : 0.01,
    'Ripple' : 0.01,
}

taxa_venda_criptos = { # Dicionário das taxas de venda das criptomoedas.

    'Bitcoin' : 0.03,
    'Ethereum' : 0.02,
    'Ripple' : 0.01,
}


bitcoin_valor = 407818
ethereum_valor = 14615
ripple_valor = 3


def linhas(texto):  # Função para decoração do texto
    print('-----------------------------------------------------------')
    print()
    print(texto)  
    print()                                                              
    print('-----------------------------------------------------------')



def login():        # Definindo a função de login do usuário
    global investidor_atual
    while True:
        cpf = input('Digite seu CPF (sem pontos e sem traços): ')
        senha = input('Digite sua senha: ')        
        if investidor.get(cpf) == senha:
            investidor_atual = cpf
            linhas('Usuário encontrado, seja bem-vindo!')
            funcao_menu()
            return
        else:
            linhas('Usuário não encontrado, Por favor, tente novamente.')


def senhas(): # Definindo a função de pedir a senha para cada operação
    senha = input('Digite sua senha para entrar nessa opção: ') 
    return senha == investidor[investidor_atual]


def funcao_menu(): # Definindo a função das opções
    linhas('Selecione uma das opções abaixo.')
    for numeros, funcoes in menu.items():
        print(f'{numeros} : {funcoes}')


def salvar_saldo(saldo): # Função para salvar o saldo do investidor 
    arquivo_saldo = f'{investidor_atual}_saldo_reais.txt'
    with open(arquivo_saldo, 'w') as arquivo:
        arquivo.write(f'{saldo:.2f}')
    

def saldo_investidor(): # Função para ver o saldo do investidor que estiver acessando a conta
    arquivo_saldo = f'{investidor_atual}_saldo_reais.txt'
    if os.path.exists(arquivo_saldo): # Caso o arquivo exista, faz uma condição
        with open(arquivo_saldo, 'r') as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo:
                return float(conteudo) if conteudo else 0.0
    else:
        return 0.0
  
 
def saldo_criptos():    # Cria um arquivo .txt dos saldos das criptomoedas         
    arquivo_saldo_criptos = f'{investidor_atual}_saldo_cripto.txt'
    saldos = {
        'Bitcoin' : 0.0, 
        'Ethereum' : 0.0,
        'Ripple' : 0.0      
}
    if os.path.exists(arquivo_saldo_criptos): 
        with open(arquivo_saldo_criptos, 'r') as arquivo:
            for linha in arquivo:
                cripto, quantia = linha.strip().split()
                saldos[cripto] = float(quantia)
    return saldos
    
def transacao(criptomoeda, quantia, preco, valor):  # Cria uma função para salvar a transação de venda ou compra no arquivo .txt
    data = datetime.datetime.now()
    extrato = f'{investidor_atual}_extrato.txt'
    with open(extrato, 'a') as arquivo:
        arquivo.write(f'{criptomoeda} {quantia} {preco} por R$ {valor:.2f} no dia {data.strftime("%x")} às BRL {data.strftime("%X")}  \n ')


def salvar_criptos(saldos): # Cria uma função para salvar os saldos das criptomoedas em um arquvio .txt
    arquivo_saldo = f'{investidor_atual}_saldo_cripto.txt'
    with open(arquivo_saldo, 'w') as arquivo:
        for criptos, preco in saldos.items():
            arquivo.write(f'{criptos} {preco:.2f}\n')

def consultar_criptos():    # Função para consultar o saldo das criptomoedas na opção 1
    arquivo_saldo = f'{investidor_atual}_saldo_cripto.txt'
    saldos = {}
    with open(arquivo_saldo, 'r') as arquivo:
        for linha in arquivo:
            criptos, preco = linha.strip().split()
            saldos[criptos] = float(preco)
        for cripto, quantidade in saldos.items():
            linhas(f'Seu saldo atual de {cripto} : {quantidade:.2f} ')


def consultar_saldo():   # Função para consultar o saldo em reais na opção 1
    saldo_atual = saldo_investidor()
    linhas(f'Seu saldo atual em reais: R$ {saldo_atual:.2f}')

def consultar_extrato():    # Função para criar um arquivo .txt que mostra o extrato da conta do investidor
    extrato = f'{investidor_atual}_extrato.txt'
    if os.path.exists(extrato):     # Caso o arquivo exista, faz uma condição
        with open(extrato, 'r') as arquivo:
            linhas('Seu extrato: ')
            for linha in arquivo:
                print(linha.strip())
    else:
        linhas('Nenhum extrato foi encontrado, tente novamente.')



def depositar(): # Criando a opção 3, que é depositar algum dinheiro na conta do investidor
    quantidade = float(input('Digite a quantidade que deseja depositar: R$ '))
    saldo_atual = saldo_investidor()
    novo_saldo = saldo_atual + quantidade
    salvar_saldo(novo_saldo)
    linhas(f'Foi depositado R${quantidade:.2f} em sua conta. Seu saldo agora é de: R${novo_saldo:.2f}')
    

def sacar(): # Criando a opção 4, que é sacar algum dinheiro da conta do investidor
    quantidade = float(input('Digite a quantidade que deseja sacar: R$ '))
    saldo_atual = saldo_investidor()

    if quantidade > saldo_atual: # Caso a quantidade que deseja sacar seja menor que a quantidade que estiver em sua conta, não será possível realizer a operação
        linhas('Você não possui saldo suficiente para sacar.')
    else:
        novo_saldo = saldo_atual - quantidade
        salvar_saldo(novo_saldo)
        linhas(f'Foi sacado R${quantidade:.2f} em sua conta. Seu saldo agora é de: R${novo_saldo:.2f}')

def comprar_cripto():   # Função para o usuário digitar o tipo de criptomoeda que deseja comprar
    while True:
        for opcoes_criptos, tipos_criptos in criptomoedas.items():
            print(f'{opcoes_criptos} : {tipos_criptos}')
        cripto = int(input('Digite o tipo de criptomoeda que deseja comprar: '))
        if cripto in criptomoedas:
            if cripto == 1:
                comprar_criptos(bitcoin_valor, 'Bitcoin')
            elif cripto == 2:
                comprar_criptos(ethereum_valor, 'Ethereum')
            elif cripto == 3:
                comprar_criptos(ripple_valor, 'Ripple')
            elif cripto == 4:
                funcao_menu()
                return
        else:
            linhas('Escolha um número válido.')

def comprar_criptos(criptos, nome_criptos): # Função para o usuário digitar a quantidade da criptomoeda selecionada que deseja comprar
    quantidade_cripto = float(input(f'Digite a quantidade de {nome_criptos} que deseja comprar: '))
    compras = quantidade_cripto * criptos
    saldo_atual = saldo_investidor()

    taxas = taxa_compra_criptos.get(nome_criptos)
    if taxas is None:
        linhas(f'Não foi encontrada a taxa para {nome_criptos}')
        return
    
    taxa = compras * taxas
    total = compras + taxa
    
    if saldo_atual >= total:
        saldo_novo = saldo_atual - total
        salvar_saldo(saldo_novo) 

        saldos_criptos = saldo_criptos()
        saldos_criptos[nome_criptos] = saldos_criptos.get(nome_criptos, 0) + quantidade_cripto
        salvar_criptos(saldos_criptos)


        transacao('Compra', quantidade_cripto, nome_criptos, compras)
        linhas(f'Parabéns, você comprou {quantidade_cripto} {nome_criptos} por R${compras:.2f}!')
    else:
        linhas('Você não possui saldo o suficiente.')

def vender_cripto():   # Função para o usuário digitar o tipo de criptomoeda que deseja vender
    while True:
        for opcoes_criptos, tipos_criptos in criptomoedas.items():
            print(f'{opcoes_criptos} : {tipos_criptos}')
        cripto = int(input('Digite o tipo de criptomoeda que deseja vender: '))
        if cripto == 1:
            vender_criptos(bitcoin_valor, 'Bitcoin')
        elif cripto == 2:
           vender_criptos(ethereum_valor, 'Ethereum')
        elif cripto == 3:
            vender_criptos(ripple_valor, 'Ripple')
        elif cripto == 4:
            funcao_menu()
            return

def vender_criptos(criptos, nome_criptos):     # Função para o usuário digitar a quantidade de criptomoeda que deseja vender
    quantidade_cripto = float(input((f'Digite a quantidade de que deseja vender: ')))
    saldos_criptos = saldo_criptos()

    
    if saldos_criptos.get(nome_criptos, 0) >= quantidade_cripto:
        vendas = quantidade_cripto * criptos


        taxas = taxa_venda_criptos.get(nome_criptos)
        taxa = vendas * taxas
        venda = vendas - taxa

        novo_saldo = saldo_investidor() + venda
        salvar_saldo(novo_saldo)

        saldos_criptos[nome_criptos] -= quantidade_cripto
        salvar_criptos(saldos_criptos)

        transacao('Venda', quantidade_cripto, nome_criptos, vendas)
        linhas(f'Parabéns, você vendeu {quantidade_cripto} {nome_criptos} por R${vendas:.2f}!')
    else:
        linhas('Você não possui criptomoedas suficientes para realizar essa venda.')

def atualizar_cotacao():
    global bitcoin_valor, ethereum_valor, ripple_valor

    data = datetime.datetime.now()
    bitcoin_valor *= random.uniform(0.95,1.05)
    ethereum_valor *= random.uniform(0.95,1.05)
    ripple_valor *= random.uniform(0.95,1.05)

    linhas(f'Cotação atual - Bitcoin: R${bitcoin_valor:.2f} | Ethereum: R${ethereum_valor:.2f} | Ripple: R${ripple_valor:.2f} ({data.strftime("%x")} às BRL {data.strftime("%X")})')


login() # Chamando a função do login do usuário

while True:
    print('')
    opcoes = int(input('Selecione uma opção do menu: ')) # Input para o usuário logado selecionar uma opção do menu
    

    if opcoes == 1:  # Função de "Consultar Saldo"
        if senhas():
            consultar_saldo()
            consultar_criptos()
        else:
            linhas('Senha inválida, tente novamente.')


    elif opcoes == 2:  # Função de "Consultar Extrato"
        if senhas():
            consultar_extrato()
        else:
            linhas('Senha inválida, tente novamente.')


    elif opcoes == 3:  # Função de "Depositar"
        if senhas():
            depositar()
        else:
            linhas('Senha inválida, tente novamente.')


    elif opcoes == 4:  # Função de "Sacar"
        if senhas():
            sacar()
        else:
            linhas('Senha inválida, tente novamente.')
            

    elif opcoes == 5:  # Função de "Comprar Criptomoedas"
        if senhas():
            comprar_cripto()
        else:
            linhas('Senha inválida, tente novamente.')


    elif opcoes == 6:  # Função de "Vender Criptomoedas"
        if senhas(): 
            vender_cripto()
        else:
            linhas('Senha inválida, tente novamente.')


    elif opcoes == 7:  # Função de "Atualizar Cotação"
        atualizar_cotacao()

    elif opcoes == 8:  # Função de "Sair"
        linhas('Volte logo!')
        exit()  # Encerra o programa

    else: # Função caso o usuário digite um número que não esteja entre 1 e 8
        linhas('Digite uma opção que esteja no menu.')

