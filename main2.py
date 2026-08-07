from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

opcao = " "
contas = []
contas_cc = []
contas_cp = []

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


        if tipo == 'CP':
            conta_poupanca = ContaPoupanca(nome, saldo)
            contas_cp.append(conta_poupanca)
            contas.append(contas_cp) # Adicionando a CP na lista CONTAS
            print(f"Parabéns {conta_poupanca.nome}, conta poupança criada com sucesso!")
            print(" ")
            #conta_poupanca.extrato_conta_poupanca()

            # printando todas as contas poupanças
            i = 0
            for conta_poupanca in contas_cp:
                contas_cp[i].extrato_conta_poupanca()
                #print(contas_cp[i])
                i+=1
            print(" ")
               
        elif tipo == "CC":
            conta_corrente = ContaCorrente(nome, saldo)
            contas_cc.append(conta_corrente)
            contas.append(contas_cc) # Adicionando a CC na lista de CONTAS
            print(f"Parabéns {conta_corrente.nome}, conta corrente criada com sucesso!")
            print(" ")
            #conta_corrente.extrato_conta_corrente()
            j = 0
            for conta_corrente in contas_cc:
                contas_cc[j].extrato_conta_corrente()
                j+=1
            print(" ")       

    if opcao == "2":
        nome = input("Digite seu nome: ")
        


print("Acabou!")