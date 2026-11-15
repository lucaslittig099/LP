#================================================================
# aluno: Lucas Rangel Littig
# matrícula: 20261EN20130
# disciplina: Linguagem de Programação
#================================================================

# Criação da classe Produto com atributos privados
class Produto:
    def __init__(self, cod, prod, prec, est):
        self.__codigo = str(cod)
        self.nome = str(prod)
        self.__preco = float(prec)
        self.__estoque = int(est)

    def venda(self, quant):
        # Verifica se há estoque e retorna o valor ou -1
        if quant > self.__estoque:
            return -1
        else:
            self.__estoque -= quant
            return quant * self.__preco

    def adiciona_estoque(self, quant):
        self.__estoque += quant

    # Métodos para acessar os atributos privados fora da classe
    def get_codigo(self):
        return self.__codigo

    def get_preco(self):
        return self.__preco
    
    def get_estoque(self):
        return self.__estoque

mercado = {}
nome_arquivo = "produtos.txt"

# Usando "a+" para evitar erro caso o arquivo não exista na primeira vez
arquivo_leitura = open(nome_arquivo, "a+")
arquivo_leitura.seek(0) # Volta ao início para ler
linhas = arquivo_leitura.readlines()

for linha in linhas:
        partes = linha.strip().split(",")
        cod = partes[0]
        prod = partes[1]
        prec = float(partes[2])
        est = int(partes[3])

        novo_produto = Produto(cod, prod, prec, est)
        mercado[cod] = novo_produto

arquivo_leitura.close()

# ETAPA 1 - CADASTRAMENTO DE PRODUTOS
while True:
    print("\n--- ETAPA 1: Cadastramento ---")
    cod_entrada = input("Insira o código (5 caracteres) ou '00000' para finalizar: ")

    if cod_entrada == "00000":
        break

    while len(cod_entrada) != 5:
        print("O código do produto deve ter exatamente 5 caracteres!!!")
        cod_entrada = input("Insira o código (5 caracteres) ou '00000' para finalizar: ")
        if cod_entrada == "00000":
            break
    
    if cod_entrada == "00000":
        break

    while cod_entrada in mercado:
        print("Esse código já foi cadastrado!!!")
        cod_entrada = input("Insira um código não cadastrado ou '00000': ")

    prod_entrada = input("Insira o nome do produto: ")
    prec_entrada = float(input("Insira o preço do produto: "))
    est_entrada = int(input("Insira a quantidade do produto no estoque: "))

    # Instancia o produto e adiciona ao dicionário
    prod_novo = Produto(cod_entrada, prod_entrada, prec_entrada, est_entrada)
    mercado[cod_entrada] = prod_novo

# ETAPA 2 - VENDA
while True:
    print("\n====MENU====")
    print("(1) Venda")
    print("(2) Sair")
    opcao = input("Insira uma das opções: ")

    while opcao != "1" and opcao != "2":
        print("Opção inválida!!!")
        print("====MENU====")
        print("(1) Venda")
        print("(2) Sair")
        opcao = input("Insira uma das opções: ")

    if opcao == "2":
        break

    print("\n--- ETAPA 2: Venda ---")
    
    total_vendas = 0 # Variável movida para cá (fora do loop de produtos)

    while True:
        cod_venda = input("Insira o código do produto ou '00000' para terminar venda: ")
        
        while cod_venda not in mercado and cod_venda != "00000":
            print("Produto não encontrado!!!")
            cod_venda = input("Insira o código do produto ou '00000' para terminar venda: ")

        if cod_venda == '00000':
            print("\n--- FIM DA VENDA ---")
            print(f"Valor total da venda: {total_vendas:.2f}")
            break # Volta ao menu inicial

        qnt_venda = int(input("Insira a quantidade para a venda: "))

        prod_atual = mercado[cod_venda]
        valor_parcial = prod_atual.venda(qnt_venda)

        if valor_parcial == -1:
            print("Não há estoque o suficiente!!!")
            print(f"Estoque atual: {prod_atual.get_estoque()}")

        else:
            total_vendas += valor_parcial
            prec = prod_atual.get_preco()
            print(f"Vendido: [Código: {cod_venda}] - Quantidade: {qnt_venda} - Preço Parcial: {valor_parcial:.2f}")

# GRAVAÇÃO NO ARQUIVO
arquivo_escrt = open(nome_arquivo, "w")

for cod_escrt in mercado:
    elemento = mercado[cod_escrt]

    prod_escrt = elemento.nome
    prec_escrt = elemento.get_preco()
    est_escrt = elemento.get_estoque()

    arquivo_escrt.write(f"{cod_escrt},{prod_escrt},{prec_escrt},{est_escrt}\n")

arquivo_escrt.close()
