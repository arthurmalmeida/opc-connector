import opclabs_quickopc
import pandas as pd

from OpcLabs.EasyOpc.DataAccess import *


opc_server = 'Kepware.KEPServerEX.V6' #OPC Server name
opc_item_id_list = ['Simulation Examples.Functions.Ramp1', 'Simulation Examples.Functions.Random1'] #Lista de tags
value = []

client = EasyDAClient() # inicia novo cliente OPC DA

#Realiza a leitura da lista de tags conectando no OPC Server
for opc_item in opc_item_id_list:
    value.append(IEasyDAClientExtension.ReadItem(client, '', opc_server, opc_item))

data_csv =  pd.DataFrame(value)

# Salvar o DataFrame no arquivo CSV
data_csv.to_csv('opc_data.csv', mode='a', index=False, encoding='utf-8')

print(f"Dados salvos")