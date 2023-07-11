from operacoes_bancarias import  menu, depositar, sacar, ler_valor, exibir_extrato, cadastrar_usuario, criar_conta, listar_contas

def main():
    LIMITE_SAQUE  = 3
    AGENCIA = "007"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    numero_conta = 1
    usuarios = []
    contas = []

    while True:
        opcao = menu().lower()

        if opcao == "d":
            valor = ler_valor()
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = ler_valor()
            saldo, extrato = sacar(
                saldo= saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUE
            )
                   
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "nc":      
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc": 
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print('Operação inválida!')

main()
