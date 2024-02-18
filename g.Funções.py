####################
######Funções#######
####################
'''
Calculando IMC
'''
#%%
imc(1.75, 75)

def imc(altura,peso):
    imc = peso/altura**2
    print("Seu IMC é", imc)

#%%
imc_retorno(1.75,80)
def imc_retorno(altura,peso):
    imc = round(peso/altura**2,1)
    return imc
    print(imc_retorno)


# %%
#Parâmetros; *args / **kwargs

def func_teste_args(param, *args):
    print("Parâmetro normal", param)
    print("Parâmetro args", args)
                                                           #Tem como saída tupla 
func_teste_args("Parametro_Normal",                        #1
           "Parametro_Args",                               #2 
           "Apesar de 2, o args consegue  passar 3")       #3
            
# %%
def func_teste_kwargs(param, **kwargs):
    print("Parâmetro normal", param)
    print("Parâmetro args", kwargs)

func_teste_kwargs("Parametro Normal", param1 = "valor1")         #Tem como saída dicionário / Aceita quantos valores forem inputados.

# %%
#LAMBDA
soma = lambda x:x+10
sub = lambda x:x-10
mult = lambda x:x*10
soma(100), sub(100), mult(100)

#%%
#Ordenando valores com Lambda
#Ordena pelo nome.
nomes = {"Python":10, "Kafka":20, "Spark":30, "Airflow":40}
sorted(nomes.items(), key=lambda x:x[0])

#Ordena pelo valor.
nomes = {"Python":10, "Kafka":20, "Spark":30, "Airflow":40}
sorted(nomes.items(), key=lambda x:x[1])

# %%
#Lambda para inverter lista
lista = [1,2,3]
inverte = lambda x:x[::-1]
inverte(lista), inverte("Python"), inverte((1,2,))     #Inverte Lista, String, Tupla
# %%
