###################
###Range###########
###Tuplas##########
###################


intervalo = range(1,10)
type(intervalo)
len(intervalo)
list(intervalo)
tuple(intervalo)

intervalo2 = range(1,10,2)                          #Define range de 1 a 10 contando de 2 em 2
list(intervalo2)                                    #Define o range como lista
intervalo2.index(5)                                 #Verifica valor no índice 5
intervalo2.count(1)                                 #Conta quantos elementos 1 existem
intervalo2.start                                    #Verifica onde o range começa
intervalo2.stop                                     #Verifica onde o range termina
intervalo2.step                                     #Verifica qual o valor do contador do range

intervalo3 = range(10,1)
intervalo4 = range(10,1,-1)

list(range(-1000,0,2))                              #Cria intervalo de -1000 a 0 porém não inclui o 0 
list(range(-1000,1,2))                              #Cria intervalo de -1000 a 0 incluindo o 0 


tpl= "janeiro", "fevereiro","março"
tpl2=("janeiro", 1, "fevereiro", 2, "março", 3)
len(tpl)
len(tpl2)
tpl[0:3]                                            #Retorna valores do índice 0 a 3
tpl.insert(5)                                       #X# TUPLAS SÂO IMUTÀVEIS
"janeiro" in tpl                                    #Verifica se elemento está em tupla

tpl3 = (("1","2","3"), (1,2,3))                     #Cria uma tupla dentro de uma tupla
len(tpl3)                                           #Indica 2 elementos

max(tpl3[1])                                        #Retorna valor máximo da segunda tupla 
min(tpl3[1])                                        #Retorna valor mínimo da segunda tupla 


tpl4=('p','y','t','h','o','n')
type(tpl4)
len(tpl4)
'''
Transformando tupla em str
'''
"-".join(tpl4)                                      #Junta os elentos da tupla com um separador

