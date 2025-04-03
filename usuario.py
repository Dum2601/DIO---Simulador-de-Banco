from banco import Banco

class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def criar_conta_corrente(self):
        numero_conta = len(self.contas) + 1
        nova_conta = Banco(agencia="0001", numero=numero_conta, usuario=self)
        self.contas.append(nova_conta)
        return nova_conta  

    def listar_contas(self):
        return self.contas

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
