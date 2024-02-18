###################
######Map##########
######Reduce#######
###################


#map = Nativo -> Utilizado para executar uma função específica função cada um item interativo
#reduce = Semelhante ao map, porém reduz a interação a um único elemento.

#%%

##Map
#%%
def convertendo_celsius_para_fahrenheit(temperatura):
    return round((float(9)/5)*temperatura + 32,2)

temp_C = [18,16,21,22,32,25,27]                        #Temperatura em Celsius

temperatura_convertida = map(convertendo_celsius_para_fahrenheit, temp_C)

list(temperatura_convertida)

#lambda

#%%
converte = lambda temperatura:round((float(9)/5)*temperatura + 32,2)
converte(21)

#%%
list(map(converte, temp_C))                             #Reduzindo a função utilizando lambda



##Reduce
from functools import reduce
import operator as op

#%%
reduce(lambda x, y: x+y, [1,2,3,4,5])                #Soma todos os valores e imprime uma saída

# %%
reduce(op.add, [1,2,3,4,5])                          #Utilizada operador op. para soma

# %%
reduce(lambda x, y: x*y [1,2,3,4,5])                  

#%%
def soma(a,b):
    resultado = a+b
    print("a", "+", "b" "=", resultado)
    return resultado
# %%
soma(3,3)
# %%
print(reduce(soma, [3,3,3,3,3]))                          