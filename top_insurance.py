import os
import json
import pandas as pd

path = 'data/top/insurance/country/india/state/' 
state_list = os.listdir(path)
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Pincode': [],
    'InsuranceCount': [],
    'SumAssured': []
}
for state in state_list:
    state_path = os.path.join(path, state)
    year_list = [year for year in os.listdir(state_path) if os.path.isdir(os.path.join(state_path, year))]
    for year in year_list:
        year_path = os.path.join(state_path, year)
        file_list = [file for file in os.listdir(year_path) if file.endswith('.json')]
        for file in file_list:
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
            if data.get('data') and data['data'].get('pincodes'):
                for record in data['data']['pincodes']:
                    clm['State'].append(state)
                    clm['Year'].append(int(year))
                    clm['Quarter'].append(int(file.strip('.json')))
                    clm['Pincode'].append(record.get('entityName'))
                    clm['InsuranceCount'].append(record.get('metric', {}).get('count', 0))
                    clm['SumAssured'].append(record.get('metric', {}).get('amount', 0))
Top_Insurance = pd.DataFrame(clm)
print(Top_Insurance)
Top_Insurance.to_csv('top_insurance.csv', index=False)
