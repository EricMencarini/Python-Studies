###################
######Datetime#####
###################

#%%
import datetime                              #Pacote de manipulação de datas e horas
from datetime import date, timedelta         ##timedelta: Variação de horários e datas

#%%
data_corrente = datetime.datetime.now()      #Mostra o horário atual completo(Da máquina)
# %%
#Convertendo string para data
data_str = "15/02/2024 08:10:01"
type(data_str)

data_convertida = datetime.datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
# %%
#Exibindo a data convertida em formatações diferentes
print(data_convertida.day)
print(data_convertida.hour)
print(data_convertida.month)
print(data_convertida.year)

# %%
data_convertida.strftime("%B")              # Retorna o Mês
data_convertida.strftime("%A")              # Retorna o dia da semana
data_convertida.strftime("%w")              # Retorna o número do dia da semana
# %%
#Criando função lambda para retornar o mês
#Facilitando chamar a função com mais praticidade.
mes = lambda x:x.strftime("%B")
mes(data_convertida)
# %%
data_convertida.time()                      # Retorna a hora/min/sec
# %%
#Utilizando timedelta
#Somando e subtraindo datas;
print("Data Atual", data_convertida)
print("10Dias Antes", data_convertida - timedelta(10))
print("10Dias Depois", data_convertida + timedelta(15))
# %%
