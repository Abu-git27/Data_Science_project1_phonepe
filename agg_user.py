import pandas as pd
import json
import os

path = 'data/aggregated/user/country/india/state/'
state_list = os.listdir(path)
clm = {
    'State': [], 
    'Year': [], 
    'Quarter': [],
    'RegisteredUsers': [], 
    'AppOpens': []
}


for state in state_list:
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                if 'data' in data and 'aggregated' in data['data']:
                    clm['State'].append(state)
                    clm['Year'].append(year)
                    clm['Quarter'].append(int(file.strip('.json')))
                    clm['RegisteredUsers'].append(data['data']['aggregated'].get('registeredUsers'))
                    clm['AppOpens'].append(data['data']['aggregated'].get('appOpens'))

Agg_User = pd.DataFrame(clm)
print(Agg_User)
Agg_User.to_csv('agg_user.csv', index=False)
