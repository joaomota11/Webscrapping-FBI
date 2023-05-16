# Webscrapping FBI
# Author: João Mota


import requests
import json

class Wanted:
    def __init__(self):
        self.api = 'https://api.fbi.gov/wanted/v1/list'
        self.attrs = ['title', 'description', 'details', 'place_of_birth', 'sex', 'dates_of_birth_used']

    def process_data(self, data):
        processed_data = []
        if 'items' in data:
            items = data['items']
            for item in items:
                processed_item = {}
                for attr in self.attrs:
                    processed_item[attr] = item.get(attr)
                processed_data.append(processed_item)
        return processed_data

    def import_data(self):
        response = requests.get(self.api)
        if response.status_code == 200:
            data = json.loads(response.content)
            processed_data = self.process_data(data)

            # Salvar os dados JSON em um arquivo
            with open('dados-fbi.json', 'w') as json_file:
                json.dump(processed_data, json_file, indent=4)

            print("Dados importados com sucesso para o arquivo 'dados-fbi.json'.")
        else:
            print("Falha na requisição.")

wanted = Wanted()
wanted.import_data()
