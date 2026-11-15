from pathlib import Path
pasta_dados = Path.cwd() / "DADOS"

# =======================================================================
# GERENCIAMENTO DE CLASSES
# =======================================================================

class ContaBancaria:
    
    total_contas_ativas = 0
    
    def __init__(self, numero, nome, saldo):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.historico = []

conta = ContaBancaria(self, saldo)
conta.__saldo = 999
        
    
    
    