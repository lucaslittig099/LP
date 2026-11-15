
from pathlib import Path

#======================================================
#ESTRUTURA DE CLASSES
#======================================================

class ContaBancaria:

    total_contas_ativas = 0

    def __init__(self, numero, nome, saldo):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = float(saldo)
        self.__historico = []
        ContaBancaria.total_contas_ativas += 1

    # Getters e Setters tradicionais (sem @property)

    def get_numero(self):
        return self.__numero

    def get_nome(self):
        return self.__nome

    def set_saldo(self, valor):
        self.__saldo = valor

    def get_historico(self):
        return self.__historico

    def aplicar_transacao(self, tipo, valor):
        valor = float(valor)
        saldo_anterior = self.get_saldo()

        if tipo == "D":
            self.set_saldo(saldo_anterior + valor)
            sucesso = True

        elif tipo == "S":
            if saldo_anterior >= valor:
                self.set_saldo(saldo_anterior - valor)
                sucesso = True

            else:
                sucesso = False
        else:
            return False

        #Registro no histórico
        if sucesso:
            self.__historico.append((tipo, valor, saldo_anterior, self.get_saldo()))

        return sucesso

    def __repr__(self):
        return f"Conta: {self.get_numero()} | Cliente: {self.get_nome()} | Saldo: {self.get_saldo():.2f}"

    def imprimir_extrato(self):
        print("\n")
        print(self.__repr__())
        print("Histórico da sessão:")
        if self.__historico == []:
            print("Nenhuma movimentação nessa sessão")
        for operacao in self.__historico:
            tipo, valor, s_ant, s_nov = operacao
            print(f"Operação: {tipo} | Valor: R$ {valor:.2f} | Saldo Anterior: {s_ant:.2f} | Saldo Novo: {s_nov:.2f}")
        print("\n")  

class ContaEspecial(ContaBancaria):
    def __init__(self, numero, nome, saldo, limite):
        super().__init__(numero, nome, saldo)
        self.__limite = float(limite)

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    #Overriding (sobrecarga de método)
    def aplicar_transacao(self, tipo, valor):
        valor = float(valor)
        saldo_anterior = self.get_saldo()

        if tipo == "D":
            self.set_saldo(saldo_anterior + valor)
            sucesso = True

        elif tipo == "S":

            if (saldo_anterior + self.get_limite()) >= valor:
                self.set_saldo(saldo_anterior - valor)
                sucesso = True
            else:
                sucesso = False
        else:
            return False

        if sucesso == True:
            self.get_historico().append((tipo, valor, saldo_anterior, self.get_saldo()))

        return sucesso

    def __repr__(self):
        # Aproveita o __repr__ da classemãe e adiciona o limite
        base_repr = super().__repr__()
        return f"{base_repr} | Limite: R$ {self.get_limite():.2f}"

# ===============================================================
# MANIPULAÇÃO DE ARQUIVOS
# ===============================================================

camin_pasta = Path.cwd() / "DADOS"
camin_pasta.mkdir(exist_ok=True)

camin_contas = camin_pasta / "contas.txt"
camin_moviment = camin_pasta / "moviment.txt"

# ===============================================================
# FLUXO PRINCIPAL
# ===============================================================

def main():
    contas_dict = {}

    # etapa 0: inicialização

    if camin_contas.exists():
        with open(camin_contas, "r") as arq:
            for linha in arq:
                dados = linha.strip().split(",")
                if len(dados) == 3:
                    # conta padrão
                    conta = ContaBancaria(dados[0], dados[1], dados[2])
                    contas_dict[dados[0]] = conta

                elif len(dados) == 4:
                    # conta especial
                    conta = ContaEspecial(dados[0], dados[1], dados[2], dados[3])
                    contas_dict[dados[0]] = conta

    print(f"\nTotal de contas ativas carregadas: {ContaBancaria.total_contas_ativas}")

    #Etapa 1: Menu Interativo

    while True:
        print("\n====MENU====")
        print("1. Criar Conta")
        print("2. Encerrar Conta")
        print("3. Saque")
        print("4. Depósito")
        print("5. Extrato")
        print("6. Finalizar")

        opcao = input("Insira uma das opções acima: ")

        if opcao == "1":
            num = input("Insira o Número da Conta(5 caracteres): ")
            if len(num) != 5:
                print("Erro: O número deve ter exatos 5 caracteres!!")
                continue
            if num in contas_dict:
                print("Erro: Essa conta já existe!!")
                continue

            nome = input("Insira o Nome do Cliente: ")
            saldo_inicial = input("Insira o Saldo Incial: ")
            tipo = input("Insira 'E' para conta especial ou 'N' para conta normal: ").upper()

            if tipo == "E":
                limite = input("Insira o limite do cheque especial: ")
                nova_conta = ContaEspecial(num, nome, saldo_inicial, limite)
            else:
                nova_conta = ContaBancaria(num, nome, saldo_inicial)

            contas_dict[num] = nova_conta
            print("Conta criada com sucesso!")

        elif opcao == "2":
            num = input("Insira o Número da Conta a ser encerrada: ")
            if num in contas_dict:
                del contas_dict[num]
                ContaBancaria.total_contas_ativas -= 1
                print("Conta encerrada!")
            else:
                print("Conta não encontrada!")

        elif opcao in ["3", "4"]:
            num = input("Insira o Número da Conta: ")
            if num in contas_dict:
                valor = float(input("Insira o valor da transição: "))
                tipo_transacao = "S" if opcao == 3 else "D"

                conta = contas_dict[num]
                # POLIMORFISMO: Não é necessário checar se é ContaBancaria ou ContaEspecial
                aprovado = conta.aplicar_transacao(tipo_transacao, valor)

                if aprovado:
                    print("Transação aprovada!!")
                    # Registrar no arquivo de log

                    with open(camin_moviment, "a") as arq:
                        arq.write(f"{num},{tipo_transacao},{valor}\n")
                else:
                    print("Recusado: Saldo Insuficiente!")
            else:
                print("Conta não encontrada!!")

        elif opcao == 5:
            num = input("Insira o Número da Conta: ")
            if num in contas_dict:
                contas_dict[num].imprimir_extrato()
            else:
                print("Conta não encontrada!!")

        elif opcao == 6:
            print("Encerrando o Sistema...")
            break

        else:
            print("Opção Inálida!!")

    #Etapa 2: Arquivamemto e Encerramento
    with open(camin_contas, "w") as arq:
        for conta in contas_dict.values():
            #obrigatório o uso do isinstance
            if isinstance(conta, ContaEspecial):
                linha = f"{conta.get_numero()},{conta.get_nome()},{conta.get_saldo()}.{conta.get_limite()}\n"
            else:
                linha = f"{conta.get_numero()},{conta.get_nome()},{conta.get_saldo()}\n"
            arq.write(linha)

    print("Dados gravados com sucesso!! Fim da execução")

if __name__ == "__main__":
    main()
  