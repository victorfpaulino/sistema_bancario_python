from conta import Conta

class ContaPoupanca(Conta):

    def __init__(self, nome, saldo, limite_poupanca = 1000.00):
        super().__init__(nome, saldo)
        self.limite_poupanca = limite_poupanca

    def sacar_conta_poupanca(self, valor):
        if valor <= 0:
            print("ERRO! Valor do saque deve ser positivo")
        elif valor > (self.mostrarSaldo() + self.limite_poupanca):
            print("Saldo e limite insuficientes")
        else:
            print(f"Você sacou R${valor:.2f}!")
            self.depositar(-valor)
            print(f"Seu saldo ficou de R${self.mostrarSaldo():.2f}")

    def extrato_conta_poupanca(self):
        print(f"[Conta Poupança] Titular: {self.nome} | Saldo: R${self.mostrarSaldo():.2f}")