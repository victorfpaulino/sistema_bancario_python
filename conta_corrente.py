from conta import Conta

class ContaCorrente(Conta):
    
    def __init__(self, nome, saldo, limite_corrente = 500.00):
        super().__init__(nome, saldo)
        self.limite_corrente = limite_corrente

    def sacar_conta_corrente(self, valor):
        if valor <= 0:
            print("ERRO! Valor do saque deve ser positivo")
        elif valor > (self.mostrarSaldo() + self.limite_corrente):
            print("Saldo e limite insuficientes")
        else:
            print(f"Você sacou R${valor:.2f}!")
            self.depositar(-valor)
            print(f"Seu saldo ficou de R${self.mostrarSaldo():.2f}")
            
    def extrato_conta_corrente(self):
        print(f"[Conta Corrente] Titular: {self.nome} | Saldo: R${self.mostrarSaldo():.2f}")