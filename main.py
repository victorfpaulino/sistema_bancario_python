from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

contas = []

conta = Conta("Victor", 200.13)
contas.append(conta)

conta = Conta("Pedrinho", 999.99)
contas.append(conta)

nome = input("Digite seu nome: ")
saldo = input("Digite o saldo: ")

conta = Conta(nome, float(saldo))
contas.append(conta)

for conta in contas:
    conta.extrato()

print("")
print("")

conta_1 = ContaCorrente("Gustavo", 500) #instanciando um obj tipo ContaCorrente
conta_1.extrato_conta_corrente()
conta_1.sacar_conta_corrente(250)
conta_1.extrato_conta_corrente()
print("")
print("")
conta_2 = ContaPoupanca("Pedro", 1000)
conta_2.extrato_conta_poupanca()
conta_2.sacar_conta_poupanca(500)
conta_2.extrato_conta_poupanca()