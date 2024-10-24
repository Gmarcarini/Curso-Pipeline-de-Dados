import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.tamanho = len(self.dados)
        self.colunas = list(self.dados[0].keys())
        self.dados = self.data_reader()
    
    def json_reader(self):
        data_json = []
        with open(self.path, 'r') as file:
            data_json = json.load(file)
        return data_json

    def csv_reader(self):
        data_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                data_csv.append(row)
        return data_csv

    def data_reader(self):
        data = []

        if self.tipo_dados == 'csv':
            data = self.csv_reader()

        elif self.tipo_dados == 'json':
            data = self.json_reader()

        return data
    
    def get_columns(self):
        return list(self.dados[0].keys())