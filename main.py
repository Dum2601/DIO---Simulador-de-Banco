from usuario import Usuario

usuarios = {}

def criar_usuario():
    nome = input("Nome: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF: ")
    endereco = input("Endereço (Logradouro, Número, Bairro, Cidade/Estado): ")

    if cpf in usuarios:
        print("Aviso: Usuário já cadastrado.")
        return
    
    usuarios[cpf] = Usuario(nome, nascimento, cpf, endereco)
    print(f"Usuário {nome} cadastrado com sucesso.")

def criar_conta():
    cpf = input("Digite o CPF do usuário: ")
    if cpf not in usuarios:
        print("Aviso: Usuário não encontrado.")
        return
    
    usuario = usuarios[cpf]
    conta = usuario.criar_conta_corrente()  # Retorna um objeto Banco

    if conta:
        print(f"Conta criada com sucesso. Agência: {conta.agencia}, Número: {conta.numero}.")

def acessar_conta():
    cpf = input("Digite o CPF do usuário: ")
    if cpf not in usuarios:
        print("Aviso: Usuário não encontrado.")
        return
    
    usuario = usuarios[cpf]
    contas = usuario.listar_contas()
    
    if not contas:
        print("Nenhuma conta encontrada para este usuário.")
        return
    
    print("Contas disponíveis:")
    for conta in contas:
        print(f"Conta: {conta.numero} (Agência {conta.agencia})")
    
    num_conta = int(input("Digite o número da conta que deseja acessar: "))
    conta = usuario.buscar_conta(num_conta)

    if not conta:
        print("Conta não encontrada.")
        return

    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("4 - Voltar ao menu principal")

        opcao = input("Opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            print(conta.deposito(valor))
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            print(conta.saque(valor))
        elif opcao == "3":
            print(conta.ver_extrato())
        elif opcao == "4":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu():
    while True:
        print("\nMenu Principal")
        print("1 - Criar Usuário")
        print("2 - Criar Conta Corrente")
        print("3 - Acessar Conta")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            acessar_conta()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    menu()
