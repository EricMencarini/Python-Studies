###################
######Classes######
###################

def criar_conta_banco(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo":saldo, "limite": limite}
    return conta

#%%
conta_eric = criar_conta_banco(1231232, "Eric", 99999, 9999)


def deposito(conta, valor):
    conta["saldo"] = conta["saldo"] + valor

def retirada(conta, valor):
    conta["saldo"] = conta["saldo"] - valor

def extrato(conta):
    print("Numero:", conta["numero"], "Saldo:", conta["saldo"], "Titular:", conta["titular"], "Limite:", conta["limite"])

def limite(conta):
    conta["limite"] = conta["limite"] + ValueError


deposito(conta_eric, 200)

extrato(conta_eric)



#%%
##Classes
class Conta_Banco():
    def __init__(self, ag, numero, titular, saldo, limite):                 #Construtor da classe/Atributos
        self.ag      = ag
        self.numero  = numero
        self.titular = titular
        self.saldo   = saldo
        self.limite  = limite

    def deposito(self, valor):
        self.saldo += valor

    def retirada(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("Ag: {} \nNúmero: {} \nTitular: {} \nSaldo: {} \nLimite {} ".format(self.ag, self.numero, self.titular, self.saldo, self.limite))

    def aumenta_limite(self, valor):
        self.limite += valor



# %%
conta_eric =  Conta_Banco(9999, 9898987, "Eric", 99999, 9999)              #Cria conta com os atributos

# %%
conta_eric.limite                                                          #Exibe limite
# %%
conta_eric.extrato()                                                       #Exibe extrato
 
