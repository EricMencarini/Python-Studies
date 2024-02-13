###################
#####Variaveis#####
#####Tipos#########
#####Operadores####
#####Métodos#######
###################

##int
idade = 33
type(idade)

idade_2 = "20"
idade_3 = "13"
idade_4 = -5
print(int(idade_2) + int(idade_3)) 
print(float(idade))

##absoluto
print(abs(idade_4))
print(round(32.8888,2))


##str
nome = "Python" 
type(nome)
nome_2 = 'Python'  ## "" ou ''

##declaração múltipla
nome_1, nome_2, nome_3 ,nome_4 = "Python", "Sql", "Scala", "Pyspark"

print(nome, nome_2)
print("Python \nPyspark")  ##Quebra Linha
print("Python \tPyspark")  ##Tabulação

sobrenome = "3.12"
print(nome, "+", sobrenome)
print((nome + " ") * 15)  ##Múltiplica Strings

testa_str = "Testando Strings"
print(testa_str[0] + testa_str[9])

print(len(testa_str)) #Número de chars
testa_str[0:16] 
testa_str[10:]
testa_str[]
testa_str[::2]  ## Slicer
testa_str[::-1] ## Inverte String

##Métodos
testa_str.zfill(20)     ## Prenche chars faltantes com 0
testa_str.endswith("s") ## Verifica último char e retorna True/False##
testa_str.endswith("Z") ##############################################
testa_str.split(" ")    #Gera lista a partir dos espaços
testa_str.count("T")    #Conta quantos "T" existem.
testa_str.upper()       #Tudo maiúsculo 
testa_str.lower()       #Tudo minúsculo
testa_str.islower()     ##Verifica tudo minúsculo
testa_str.capitalize    #Primeira metra maiúscula


##float
versao = 3.12
type(versao)






