class Conta:

    def __init__ (self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo # variável privada
    
    # SETS
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if (valor > self.__saldo):
            print("Saldo insuficiente!")
        elif (valor < self.__saldo):
            self.__saldo -= valor

    def extrato(self):
        #print("Saldo: " + self.__saldo)
        print(f"Titular: {self.nome} | Saldo: R${self.__saldo:.2f}")

    
    # GET
    def mostrarSaldo(self):
        return float(self.__saldo)


