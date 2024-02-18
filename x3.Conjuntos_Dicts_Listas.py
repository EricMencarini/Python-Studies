###################
#######Sets########
#######Dicts#######
#######Listas######
###################


conjunto1 ={"python", "pyspark", "scala"}
conjunto2 ={"docker", "kafka", "zookepeer","python"}
type(conjunto1)
type(conjunto2)


conjunto3 =conjunto1.intersection(conjunto2)
conjunto4 = conjunto1.union(conjunto2)


#métodos
conjunto1.discard("python")     #Remove elemento
conjunto1.add("python")            #Adiciona elemento
conjunto1.remove("python")      #Similar ao discard porém exibe erro se elemento não existe.
conjunto1.issubset({"pyspark"}) #Elemento contém o set.(boleano)
{"pyspark"}.issubset(conjunto1) #Set contém o elemento.(boleano)
conjunto1.pop()                 #Remove primeiro elemento do set


'''
Transformando lista em set para ordenar e remover duplicados.
'''
conjunto_duplicado =[2,6,1,5,7,3,0,8,4,9,9,10,1,0,11,4,3,7,6,5]
len(conjunto_duplicado)
set(conjunto_duplicado)

perifericos = {"teclado": 400, "mouse":200, "headset": 600} #Cria dict
perifericos.keys()                                         #Retorna chaves 
perifericos.values()                                       #Retorna valores
perifericos.items()                                        #Retorna itens

#%%
dic1 = {}                                                  #Cria dict vazio
dic1["python"]=3.11
dic2 ={}
dic2["dia_da_semana"] = "segunda","terça","quarta","quinta","sexta"
dic2["meses_do_ano"] = "jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"
print(dic2["dia_da_semana"])

#%%
dic3 = {}
dic3["meses_do_ano"] = {}
dic3["meses_do_ano"]["jan"] = 1
dic3["meses_do_ano"]["fev"] = 2
dic3["meses_do_ano"].keys()                                #Retorna só os meses.
dic3["meses_do_ano"].values()                              #Retorna só os valores dos meses.

#%%
#Métodos
dic1.pop("python")                                         #Remove elemento 
sorted(dic2)                                               #Ordena pelos valores Dia -> Meses
dic3.get("meses_do_ano")                                   #Retorna nome/valor dos meses


#%%
lista1 = [1,2,5,-1,-2,999]

#%%
type(lista1)
len(lista1)                                               #Conta char
lista1[3]                                                 #Verifica item, índice3
lista1[5] = 3000                                          #Adiciona elemento 3000 no índice 5

#%%
lista1.insert(10,200)                                     #Insere 200 no índice10
lista1.remove(2)                                          #Remove elemento 2
lista1.sort()                                             #Ordena lista
lista1.sort(reverse=True)                                 #Ordena lista decrescentemente                           
3000 in lista1                                            #Verifica se elemento existe na lista
#%%
lista1 + [1,2,3]                                          #Soma duas listas
#%%
lista1.append(5,6,7)                                      #Adiciona lista dentro de lista
lista1.extend(8,9,10)                                     #Adiciona valores dentro da lista
lista1[-4].append(8)                                      #Busca o índice em que existe a sublista e adiciona o valor 8
lista1[:6]                                                #Busca os valores até o  índice 6
max(lista1[:6])                                           #Busca o maior valor entre os índices  selecionados
min(lista1[:6])                                           #Busca o menor valor entre os ínidices selecionados

# %%
