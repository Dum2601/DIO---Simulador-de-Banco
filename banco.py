class Banco:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def deposito(self, valor_depositado):
        if valor_depositado > 0:
            self.saldo += valor_depositado
            self.extrato.append(f'Depósito: R$ {valor_depositado:.2f}')
            return f'Depósito de R$ {valor_depositado:.2f} efetuado!'
        
        return 'O valor informado não pode ser negativo ou zero!'

    def saque(self, valor_saque):
        if valor_saque > self.saldo:
            return 'Saldo insuficiente!'
        
        elif valor_saque > self.limite:
            return f'Não é possível sacar mais de R$ {self.limite:.2f} por vez!'
        
        elif self.numero_saques >= self.LIMITE_SAQUES:
            return f'Limite de {self.LIMITE_SAQUES} saques diários alcançados!'
        
        elif valor_saque > 0:
            self.saldo -= valor_saque
            self.extrato.append(f'Saque: R$ {valor_saque:.2f}')
            self.numero_saques += 1
            return f'Saque de R$ {valor_saque:.2f} efetuado!'
        
        return 'Valor inválido!'

    def ver_extrato(self):
        if self.extrato:
            extrato_str = '\n'.join(self.extrato)
            return f'\n\n{'='*30}\n\nExtrato:\n{extrato_str}\n\nSaldo atual: R$ {self.saldo:.2f}\n\n{'='*30}\n\n'
        
        return 'Não foram realizadas movimentações!'


banco = Banco()
print(f'\n\n{'='*30}\n\n')
print(banco.deposito(100))  
print(banco.saque(20))
print(banco.ver_extrato())  
