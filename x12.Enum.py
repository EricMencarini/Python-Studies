###################
#####Enumerate#####
###################

##Função built-in recebendo objeto interável utilizado pra retornar ID.

#%%
lista = ["a","b","c"]
list(enumerate(lista))                              #Imprime [(0, 'a'), (1, 'b'), (2, 'c')]

list(enumerate(lista, start =-10))                  #Inicia o ID em -10

meses = "janeiro", "fevereiro", "março", "abril", "maio","junho"

#Imprimindo numero do mês em um FOR
cont = 1
for mes in meses:
    print("Mes", mes, "Numero:", cont)
    cont+=1
    print("numero do mes",)

#%%
#Usando o enumerate
for num, mes in enumerate(meses, start=1):           #Otimização do código e estrutura mais clean.
    print("Mes:", mes, "=", num)


# %%
