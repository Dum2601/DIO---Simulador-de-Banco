class Usuario:
    pass
    # Armazenar os dados em uma lista (nome, data de nascimento, cpf(apenas 1 é possível por usuário) e endereço(String com o formato: logradouro, numero, bairro, cidade/Sigla estado))
    def __init__(self, nome, nascimento, cpf, endereço):
        self._nome = nome # str
        self.__nascimento = nascimento # str
        self.__cpf = cpf #str
        self.__endereco = endereço #str
        self._n_agencia = '0001' #str
        self.__num_conta = 0
        
    # Métodos
    
    # Criar Conta corrente
    # Deve armazenar contas em uma lista (Colocar como dicionário). Ela é composta por: Agência (fixo como 001), número da conta (sequencial começando com 1) e usuário (Pode ter mais de uma conta)
    
 