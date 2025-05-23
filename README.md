# Projeto FEI 1° Semestre Ciências da Computação - Exchange de Criptomoedas em Python

1.  Introdução.
    O propósito do projeto é desenvolver uma Exchange de criptomoedas que realiza um login, consultar seu saldo, consultar seu extrato, realizar depósitos e saques, compra e venda de criptomoedas e visualizar a cotação atual.
    Exchange de criptomoedas consiste em uma plataforma virtual onde é realizado operações de vendas e compras de criptomoedas com Dólar ou Real, para este trabalho, utilizamos o Real.
    Criptomoeda é um tipo de dinheiro criptografado que consiste em ser totalmente virtual, além de ser livre de taxas do governo. Utilizamos as seguintes criptomoedas: 

        •	Bitcoin (BTC): Criada em 2009, é a primeira criptomoeda feita e a mais famosa. Sua cotação atual (04/11/2024 BRL 14:30) é de R$391.029,00.

        •	Ethereum (ETH): Lançada em 2015, é uma criptomoeda usada em uma blockchain chamada Ethereum, que permite a realização de contratos inteligentes e transações. Sua cotação atual (04/11/2024 BRL 14:33) é de R$13.996,50.

        •	Ripple (XRP): Lançada em 2012, foi criada para facilitar as transações financeiras, como transferências internacionais que podem demorar muito para serem realizadas e passível de taxações. Sua cotação atual (04/11/2024 BRL 14:39) é de R$2,93.


2.	Documentação.

    2.1 – Tecnologias utilizadas.
    Para desenvolver o projeto, foi usado a linguagem de programação Python e suas bibliotecas, sendo elas:

        •	“datetime”: Consiste na manipulação de datas e horários do sistema.

        •	“random”: Importa números aleatórios para a manipulação dos preços das criptomoedas.

        •	“os”: Ajuda na manipulação de leitura e escrita de arquivos.

    2.2 – Estrutura.
    A estrutura do projeto é composta por dois arquivos, sendo eles:

        •	“projeto.py”: Arquivo que contém todo o código do sistema.

        •	“extrato.txt”: Arquivo utilizado para salvar o saldo do investidor atual.

        •	“saldo_cripto.txt’: Arquivo que salva o seu saldo atual de criptomoedas.

        •	“saldo_reais.txt”: Arquivo que salva o seu saldo atual de Real.

    2.3	– Funções do código.
    O projeto consiste em várias funções, sendo elas:

        2.3.1.	Login e autenticação do usuário:

        •	“login()”: Consiste no usuário digitar seu CPF e sua senha, caso as credenciais estejam de acordo, exibe o menu do Exchange. Caso contrário, a senha é solicitada novamente até o usuário acertá-la.

        •	“senhas()”: Consiste em que cada vez que o usuário escolher uma opção, solicite a senha do mesmo.

        2.3.2.	Salvar e armazenar saldos e dados do usuário.
        Para realizarmos transações, saque, depósitos, compras ou vendas, é necessário um arquivo .txt que armazena todas essas opções, para isso, foi criado as seguintes funções:

        •	“salvar_saldo(saldo)”: Esta função faz com que o saldo do investidor seja atualizado cada vez que fizer uma transação, compra ou venda, em Reais, no arquivo “{investidor_atual}_saldo_reais.txt”.

        •	“salvar_criptos(saldo)”: Semelhante a função de salvar o saldo do investidor, porém com criptomoedas e armazenado no arquivo “{investidor_atual}_saldo_cripto.txt”


        •	“saldo_investidor()”: Faz com que o saldo seja mostrado no mesmo arquivo da função acima, em Reais.


        •	“saldo_criptos()”: Basicamente a mesma função de mostrar o saldo do investidor no arquivo .txt, só que com as criptomoedas.

        •	“transacao(criptomoeda, quantia, preco, valor)”: Função criada para realizar transação exibindo o tipo (compra ou venda), criptomoeda selecionada, quantidade, preço de cada uma e valor total. 

        2.2.3.	Funções do menu.

        •	“consultar_saldo()” e “consultar_criptos()”: Essas funções fazem com que o saldo de Real e o saldo de criptomoedas é mostrado no terminal.

        •	“comprar_cripto()”: Essa função consiste no usuário selecionar o tipo de criptomoeda que deseja comprar.

        •	“comprar_criptos()”: Consiste no usuário escolher a quantidade da criptomoeda selecionada pelo mesmo ele deseja comprar. Caso o usuário não tenha dinheiro suficiente, exibe uma mensagem informando-o.

        •	“vender_cripto()”: Essa função consiste no usuário selecionar o tipo de criptomoeda que deseja vender. 	

        •	“vender_criptos()”: Consiste no usuário escolher a quantidade da criptomoeda selecionada pelo mesmo ele deseja vender. Caso o usuário não tenha a quantidade digitada, é solicitado novamente um valor que esteja na conta do investidor.

        •	“atualizar_cotacao()”: Atualiza a cotação das criptomoedas cada vez que o usuário seleciona a opção. Uma vez atualizada, a cotação é variada entre no máximo +5% e no mínimo -5% do valor antigo. 
		
        2.2.4.	Dicionários utilizados.
        Para um melhor controle de dados e de organização dentro do código, foi usado dicionários, sendo eles:
        •	“investidor”: Determina os dados do investidor que estiver utilizando a Exchange, por meio de seu CPF e senha.

        •	“menu”: Dicionário criado para fazer as opções do menu principal.

        •	“criptomoedas”: Dicionário que exibe as opções de seleção das criptomoedas.

        •	“taxa_compra_criptos”: Consiste em um dicionário que aplica as taxas de compra para as respectivas criptomoedas.

        •	“taxa_venda_criptos”: Semelhante ao dicionário citado acima, porém com a diferença de que aplica as taxas de venda das criptomoedas.

3.	Testes realizados e resultados.
Para garantir o melhor funcionamento do programa, foi realizado os seguintes testes:

    •	Login feito com credenciais inválidas e válidas.

    •	Testes feito com saldos positivos e negativos, para confirmar que não terá nenhum saldo negativo na conta.

    •	Testes feitos das taxas aplicadas nas compras e vendas das criptomoedas.

    •	Verificação da atualização da cotação dos preços das criptomoedas.

O resultado dessas operações foi conforme esperado e o sistema executou suas devidas mensagens de erro quando foi necessário.
