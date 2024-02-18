###################
######Herança######
###################

#Definindo classe principal.

class Conta_Base():
    def __init__(self, ag, numero, titular, saldo, limite):     
        self.ag      = ag            
        self.numero  = numero
        self.titular = titular
        self.saldo   = saldo
        self.limite  = limite

    def deposito(self, valor):
        novo_saldo = self.saldo + valor
        self.saldo += valor

    def retirada(self, valor):
        novo_saldo = self.saldo - valor
        self.saldo -= valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para o saque {} -- Escolha outro valor".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo    

    def extrato(self):
        print("Ag: {} \nNúmero: {} \nTitular: {} \nSaldo: {} \nLimite {} ".format(self.ag, self.numero, self.titular, self.saldo, self.limite))

    def aumenta_limite(self, valor):
        self.limite += valor


conta1 = Conta_Base('123', '123123', "X", 999, 999)
conta1.extrato()
conta1.retirada(1000)



#Herança
class ContaPoupanca(Conta_Base):
    def __init__(self, ag, numero, titular, saldo, limite, rendimento):
        super().__init__(ag, numero, titular, saldo, limite)     
        self.rendimento = rendimento

   
conta_eric_poup = ContaPoupanca('123', '123123', "X", 999, 999, 0.025)
conta_eric_poup.rendimento
conta_eric_poup.numero



class ContaSalario(Conta_Base):
    def __init__(self, ag, numero, titular, saldo, limite, salario):
        super().__init__(ag, numero, titular, saldo, limite)     
        self.rendimento = salario

    def receber(self):
        self.deposito(self.salario)

    def novo_salario(self, novo_salario):
        self.salario = novo_salario    

conta_eric_sal = ContaPoupanca('123', '123123', "X", 999, 999, 50000)



class ContaCorrente(Conta_Base):
    def __init__(self, ag, numero, titular, saldo, limite):
        super().__init__(ag, numero, titular, saldo, limite)     
        limite = 0 if limite < 0 else limite                       
        self.limite = limite

    def retirada(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo + self.limite < 0:
            print("Limite de {} insuficiente para saque de {}. Saldo Atuaç {}".format(self.limite + self.saldo, valor, self.saldo))
        else:
            self.saldo = novo_saldo

    def extrato(self):
        print("Ag: {} \nNúmero: {} \nTitular: {} \nSaldo: {} \nLimite {} \nSaldo&Limite {} ".format(self.ag, self.numero, self.titular, self.saldo, self.limite, self.saldo+self.limite))

    def novo_salario(self, novo_salario):
        self.salario = novo_salario    

conta_eric_sal = ContaCorrente('1233', '1231231', "X", 674, 365)

conta_eric_sal.extrato()



