import opclabs_quickopc
import pandas as pd

from OpcLabs.EasyOpc.DataAccess import *


opc_server = 'Kepware.KEPServerEX.V6'
opc_item_id_list = ['Simulation Examples.Functions.Ramp1', 'Simulation Examples.Functions.Random1']
opc_item_id = 'Simulation Examples.Functions.Ramp1'
value = []

client = EasyDAClient()
#value = IEasyDAClientExtension.ReadItemValue(client, '', opc_server, opc_item_id)

for opc_item in opc_item_id_list:
    value.append(IEasyDAClientExtension.ReadItem(client, '', opc_server, opc_item))

data_csv =  pd.DataFrame(value)

# Salvar o DataFrame no arquivo CSV
data_csv.to_csv('opc_data.csv', mode='a', index=False, encoding='utf-8')

print(f"Dados salvos")