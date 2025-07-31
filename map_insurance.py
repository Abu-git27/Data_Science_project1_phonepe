import pandas as pd
import json
import os

path = 'data/map/insurance/country/india/state/'
state_list = os.listdir(path)
clm = {
    'State': [], 
    'Year': [], 
    'Quarter': [],
    'District': [], 
    'InsuranceCount': [], 
    'SumAssured': []
}

for state in state_list:
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                if data.get('data') and data['data'].get('data') and isinstance(data['data']['data'], dict):
                    for entry in data['data']['data'].get('data', []):
                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['District'].append(entry[3] if len(entry) > 3 else None)
                        clm['InsuranceCount'].append(entry[2] if len(entry) > 2 else None)
                        clm['SumAssured'].append(None)

Map_Insurance = pd.DataFrame(clm)
print(Map_Insurance)
Map_Insurance.to_csv('map_insurance.csv', index=False)
