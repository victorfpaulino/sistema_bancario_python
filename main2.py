#from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

opcao = " "
contas = []


while opcao != "3":

    print("********** BANK **********")
    print("1. Criar conta")
    print("2. Logar")
    print("3. Sair")
    print("**************************")
    opcao = input("Entre com uma das opções: ")

    if opcao == "1":
        print("Bem-vindo(a) ao BANK!")
        nome = input("Digite seu nome: ")
        saldo = float(input("Digite o saldo a ser depositado: R$"))
        tipo = input("Digite o tipo de conta: 'CP' para Poupança e 'CC' para Corrente: ")
        print(" ")

        # Se for Conta Poupança
        if tipo == 'CP':
            conta_poupanca = ContaPoupanca(nome, saldo)
            contas.append(conta_poupanca)
            print(f"Parabéns {conta_poupanca.nome}! Sua conta poupança foi criada com sucesso!")
            conta_poupanca.extrato_conta_poupanca()
            print(" ")

        # Se for Conta Corrente
        elif tipo == "CC":
            conta_corrente = ContaCorrente(nome, saldo)
            contas.append(conta_corrente)
            print(f"Parabéns {conta_corrente.nome}! Sua conta corrente foi criada com sucesso!")
            conta_corrente.extrato_conta_corrente()
            print(" ")       

    if opcao == "2":
        print("*** LOGIN ***")
        nome_login = input("Digite seu nome: ")
        print(" ")
        conta_logada = None

        for obj in contas:
            if obj.nome == nome_login:
                conta_logada = obj
                print("Login efetuado com sucesso!")
                print(" ")
                break

        if conta_logada is None:
            print("ERRO! Usuário não encontrado!")
        else:
            print("O que deseja fazer?")
            print("1. Ver extrato")
            print("2. Sacar")
            print("3. Depositar")
            print("4. Sair")

            op = input("Entre com a opção desejada: ")

            if op == "1":
                if conta_logada is conta_poupanca:
                    conta_logada.extrato_conta_poupanca()
                elif conta_logada is conta_corrente:
                    conta_logada.extrato_conta_corrente()

            elif op == "2":
                if conta_logada is conta_poupanca:
                    valor = float(input("Qual valor deseja sacar? R$"))
                    conta_logada.sacar_conta_poupanca(valor)
                elif conta_logada is conta_corrente:
                    valor = float(input("Qual valor deseja sacar? R$"))
                    conta_logada.sacar_conta_corrente(valor)

            elif op == "3":
                   valor = float(input("Qual valor deseja depositar? R$"))
                   conta_logada.depositar(valor)

            elif op == "4":
                break


print("Acabou!")