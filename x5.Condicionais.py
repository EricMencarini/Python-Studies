###################
###Condicionais####
###################

idade = 18

if idade >= 18:
    print("Você pode tirar sua CNH")
elif idade == 17:
    print("Falta um ano para tirar a CNH") 
else:
    print("Aguarde chegar aos 18 anos")


'''
Input básico com login e senha
'''
#%%  -- Define notebook no vscode
nome = input("Digite seu nome:")
senha = input("Digite sua senha")
password=123456

if nome == "admin" and int(senha) == password: 
    print("Logado como admin")
elif password == int(senha):
    print("Login com sucesso")
else:
    print("Senha incorreta")


#%%
'''    
Verificando par ou impar
'''
numero = input("Digite seu numero: ")
if int(numero)%2 ==0:
    print("par")
else:
    print("impar")    

#%%
##if ternário
numero = input("Digite seu numero:")
"par" if int(numero)%2==0 else "impar"

#%%
#Verifica se número é divisivel por 2,3,5 e faz tratamentos
print("Verifica se o número é divisivel por 2,3,5")
print("Digite seu número:")
numero = int(input())
contador = 0
if numero%2 == 0:
    print("O numero é divisivel por 2")
    contador+=1
if numero%3 == 0:
    print("O numero é divisivel por 3")
    contador+=1
if numero%5 == 0:
    print("O numero é divisivel por 5")
    contador+=1   
if contador == 0:   
    print("Não é divisivel por:(2,3,5)")
# %%
