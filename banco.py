class Banco:
    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return f"Depósito de R$ {valor:.2f} efetuado!"
        return "O valor informado não pode ser negativo ou zero!"

    def saque(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente!"
        elif valor > self.limite:
            return f"Não é possível sacar mais de R$ {self.limite:.2f} por vez!"
        elif self.numero_saques >= self.LIMITE_SAQUES:
            return f"Limite de {self.LIMITE_SAQUES} saques diários alcançados!"
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            return f"Saque de R$ {valor:.2f} efetuado!"
        return "Valor inválido!"

    def ver_extrato(self):
        if self.extrato:
            extrato_str = "\n".join(self.extrato)
            return f"\n{'='*30}\nExtrato:\n{extrato_str}\nSaldo atual: R$ {self.saldo:.2f}\n{'='*30}"
        return "Não foram realizadas movimentações!"
