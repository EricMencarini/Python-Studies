###################
######Loops########
###################

#FOR
for numero in range(0,10):
    print("O numero é:", numero) 

#%%
#Imprime o loop com a condicional de verificação se é par ou ímpar
for numero in range(0,10):
    if numero%2==0:
        print(numero, "É par")
    else:
        print(numero, "É impar")
# %%
#Define contador para gerar a saída de cada mês
meses = "jan", "fev", "mar", "abr", "mai", "jun"
for mes in meses:
    print(mes)

# %%
#Define o break para parar o loop ao chegar em determinado mês
for mes in meses:
    print(mes)
    if mes == "mai":
        break

#%%
#WHILE
numero = 0
while(numero < 10):
    numero+= 1              #contador para cada loop
    print(numero)
# %%
#Verifica par ou ímpar com while
numero =0
while(numero<10):
    if numero%2==0:
        print(numero, "É par")
    else:
        print(numero, "É Impar")
    numero+=1    
# %%
numero = 0
while(numero<10):
    numero+=1
    print("Mensagem:", numero)

# %%
#CONTINUE 
numero=0
while(numero<10):
    numero+=1
    if numero%2!=0:
        continue                 #Ignora o procedimento do código e retorna para o ínicio
    print("Seu número par é:", numero)
# %%
'''
Busca número digitado pelo usuário entre 1 a 10;
'''
numero_input = int(input("Digite um numero de 1 a 10:"))
numero_usuario = -1
while(numero_usuario != numero_input):
    if numero_input > 10:
        numero_input = int(input("Digite um numero de 1 a 10"))
    elif numero_input <= 0:
        numero_input = int(input("Digite um numero de 1 a 10"))    
    else:
        numero_usuario+=1
        if numero_usuario == numero_input:
            print("O numero que você digitou foi:", numero_usuario)
        else:
            print("Ainda não descobri seu número")
# %%
