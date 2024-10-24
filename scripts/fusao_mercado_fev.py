import json
import csv
from processamento_dados import Dados


#Funções
def json_reader(path_json):
    data_json = []
    with open(path_json, 'r') as file:
        data_json = json.load(file)
    return data_json

def csv_reader(path_csv):
    data_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            data_csv.append(row)
    return data_csv

def data_reader(path, type):
    data = []

    if type == 'csv':
        data = csv_reader(path)

    elif type == 'json':
        data = json_reader(path)

    return data

def get_columns(data):
    return list(data[0].keys())

def rename_columns(data, key_mapping):
    new_data_csv = []

    for dict in data:
        dict_temp = {}
        for chave,valor in dict.items():
            dict_temp[key_mapping[chave]] = valor
        new_data_csv.append(dict_temp)

    return new_data_csv

def size_data(data):
    return len(data)

def join(dataA, dataB):
    data = []
    data.extend(dataA)
    data.extend(dataB)
    return data

def tranform_data_table(data, columns_name):
    processed_data = []

    processed_data.append(columns_name)

    for item in data:
        row = []
        for name in columns_name:
            row.append(item.get(name, 'Indisponível'))
        processed_data.append(row)

    return processed_data

def save_data(data, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


#Caminho para os Dados
path_json = 'data_raw/dados_empresaA.json'

path_csv = 'data_raw/dados_empresaB.csv'

path_processed_data = 'data_processed/dados_processados.csv'

dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')


'''#Variaveis de Dados Brutos
json_raw_data = data_reader(path_json, 'json')
json_name_columns = get_columns(json_raw_data)
json_data_size = size_data(json_raw_data)
print(json_raw_data[0])

csv_raw_data = data_reader(path_csv, 'csv')
csv_name_columns = get_columns(csv_raw_data)
csv_data_size = size_data(csv_raw_data)
print(csv_raw_data[0])


#Alteração dos Dados
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

csv_raw_data = rename_columns(csv_raw_data, key_mapping)

fusion_data = join(csv_raw_data, json_raw_data)
fuison_columns_name = get_columns(fusion_data)

#Salvando Dados
fusion_data_table = tranform_data_table(fusion_data, fuison_columns_name)
save_data(fusion_data_table, path_processed_data)'''