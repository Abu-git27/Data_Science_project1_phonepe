import pandas as pd
import json
import os

path = 'data/map/transaction/hover/country/india/state/'
state_list = os.listdir(path)
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'TransactionCount': [],
    'TransactionAmount': []
}

for state in state_list:
    state_path = os.path.join(path, state)
    year_list = os.listdir(state_path)

    for year in year_list:
        year_path = os.path.join(state_path, year)
        file_list = os.listdir(year_path)

        for file in file_list:
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                if data.get('data') and 'hoverDataList' in data['data']:
                    for entry in data['data']['hoverDataList']:
                        district = entry.get('name')
                        metric_data = entry.get('metric', [{}])[0]
                        count = metric_data.get('count')
                        amount = metric_data.get('amount')

                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['District'].append(district)
                        clm['TransactionCount'].append(count)
                        clm['TransactionAmount'].append(amount)

Map_Transaction = pd.DataFrame(clm)
print(Map_Transaction)
Map_Transaction.to_csv('map_transaction.csv', index=False)
