####################
######Filter########
########Zip#########
#List Comprehension#
####################


#Filter, bem similar ao map e ao reduce porém com literalmente um uso de filtro para testar se uma função é retornável

#%%
num = list(range(0,10))
num

# %%
Par = lambda x: True if x%2==0 else False                        #Verifica se é par
Par(3)
# %%
list(filter(Par, num))                                           #Dentro da lista[0,10] verifica quem é par

# %%
num2 = list(range(0,9999))
num2
Par2 = lambda x: True if x%100==0  else False                    #Verifica números pares divisíveis por 100 
list(filter(Par2,num2))                                           
# %%


#Zip, função utilizada para fazer junções de listas.

#%%
lista1= ["a","b","c"]
lista2= [1,2,3]
list(zip(lista1, lista2))                                       #Gera tuplas como saída
# %%
lista3=["a1","a2","a3","a4"]                                    #Juntando uma lista com um elemento a mais. O 4 elemento é discartado.
lista4=["x","z"]
juncao = list(zip(lista1,lista2,lista3,lista4))                 #A quantidade elementos na saída será a lista com a menor quantidade de valores.

# %%
len(juncao)


#List Comprehension, funciona com uma ideia similar ao FOR através de uma lista vazia;

'''
Executando a mesma função com map, for e list comprehension
'''
#%%
def convertendo_celsius_para_fahrenheit(temperatura):
    return round((float(9)/5)*temperatura + 32,2)                      #Map
temp_C = [18,16,21,22,32,25,27]  
list(map(convertendo_celsius_para_fahrenheit, temp_C))

#%%
temp_C2= []
for temp in temp_C:
    nova_temp = convertendo_celsius_para_fahrenheit(temp)              #For
    temp_C2.append(temp_C2)
    print(nova_temp)


#Código super clean, otimizado que já retorna a função como lista.
# %%
[convertendo_celsius_para_fahrenheit(temp) for temp in temp_C]         #List Comprehension

#Utilizando condicionais.
# %%
[convertendo_celsius_para_fahrenheit(temp) for temp in temp_C if temp > 30]

#Serve para como dict comprehension.
# %%
tpl ={"janeiro":1, "fevereiro":2, "março":3}

#%%
for item in tpl:
    tpl[item] = tpl[item]*2    
print(tpl)

# %%
{item:tpl[item]*2 for item in tpl}
