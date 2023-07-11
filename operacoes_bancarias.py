import textwrap

def menu():
   
    menu = f"""
    {30 * '='+'MENU'+ 30 * '='}
    Informe a operação que deseja realizar:

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [nu]\tNovo usuário
    [lc]\tListar contas
    [q]\tSair

    : """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f"Deposito no valor de R$ {valor:.2f}\n")
    else:
        print('Operação falhou! O valor informado é invalido.')
    return saldo, extrato

def ler_valor():
    return float(input('Digite o valor do depósito: '))

def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques > limite_saques

    if excedeu_saldo:
        print('\nDesculpe! Você não tem saldo em conta suficiente.')
    elif excedeu_limite:
        print('\nDesculpe! Você ultrapassou o valor limite por saque.')
    elif excedeu_saques:
        print('\nDesculpe! Você ultrapassou o numéro de saques diários.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n' 
        num_saques += 1
        print(f"Saque no valor de R$ {valor}")
        return saldo, num_saques, extrato
    else:
        print('Desculpe! Valor inválido.')

def exibir_extrato(saldo, /, *, extrato):
    print(f"\n{15*'='}EXTRATO{15*'='}")
    print('Não há movimentações em sua conta.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print(f"\n{(30 + len('extrato')) *'='}")

def cpf_existente(usuarios, cpf):
    return cpf in [usuario['cpf'] for usuario in usuarios]

def cadastrar_usuario(usuarios):
    cpf = input('Entre com o CPF do novo usuário (somente números): ')

    if cpf_existente(usuarios, cpf):
        print("\nJá existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n°, bairro, cidade/UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("===Cadastro realizado com sucesso!===")
    return usuarios

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = {}

    if cpf_existente(usuarios, cpf):
        print("\nConta criada com sucesso!")
        for user in usuarios:
            if user["cpf"] == cpf:
                usuario = user
        return {"agencia": agencia, "conta": numero_conta, "usuario": usuario}
    
    print("CPF não cadastrado! Por favor cadastre o usuário!!")
    return None


def listar_contas(contas):
    if not contas:  
        print("===Não há contas cadastradas!===")
        return
    
    for conta in contas:
        dado = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t{conta['conta']}
                Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 50)
        print(textwrap.dedent(dado))