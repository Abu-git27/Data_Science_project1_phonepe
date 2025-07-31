import pandas as pd
import json
import os

path = 'data/aggregated/insurance/country/india/state/'
state_list = os.listdir(path)
clm = {
    'State': [], 
    'Year': [], 
    'Quarter': [],
    'Transaction_type': [],
    'Transaction_count': [], 
    'Transaction_amount': []
}

for state in state_list:
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                if 'data' in data and 'transactionData' in data['data']:
                    for record in data['data']['transactionData']:
                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['Transaction_type'].append(record['name'])
                        clm['Transaction_count'].append(record['paymentInstruments'][0]['count'])
                        clm['Transaction_amount'].append(record['paymentInstruments'][0]['amount'])

Agg_Insurance = pd.DataFrame(clm)
print(Agg_Insurance)
Agg_Insurance.to_csv('agg_insurance.csv', index=False)
