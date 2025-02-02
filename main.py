import opclabs_quickopc
import pandas as pd
import csv

from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


opc_server = 'Kepware.KEPServerEX.V6' #OPC Server name
opc_item_id_list = ['Simulation Examples.Functions.Ramp1', 'Simulation Examples.Functions.Random1'] #Lista de tags
value = []
multiple = []

client = EasyDAClient() # inicia novo cliente OPC DA

#Realiza a leitura da lista de tags conectando no OPC Server
for opc_item in opc_item_id_list:
    value.append(IEasyDAClientExtension.ReadItem(client, '', opc_server, opc_item))

data_csv =  pd.DataFrame(value)

#salvar dados no csv
data_csv.to_csv('opc_data.csv', mode='a', index=False, encoding='utf-8')

print("Gravou dados da chamada individual")

#Le Multilos Valores
multiple_values = IEasyDAClientExtension.ReadMultipleItems(client,
    ServerDescriptor('Kepware.KEPServerEX.V6'),
    [
        DAItemDescriptor('Simulation Examples.Functions.Ramp1'),
        DAItemDescriptor('Simulation Examples.Functions.Ramp2'),
        DAItemDescriptor('Simulation Examples.Functions.Random1'),
        DAItemDescriptor('Simulation Examples.Functions.Random2')
    ])

# grava os valores em uma lista para transformar em um data frame
for i, Result in enumerate(multiple_values):
    assert Result is not None
    multiple.append(Result.Vtq)

data_csv2 =  pd.DataFrame(multiple)

#salvar dados no csv
data_csv2.to_csv('opc_data2.csv', mode='a', index=False, encoding='utf-8')

print("Gravou dados da chamada em lista")