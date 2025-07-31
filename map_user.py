import pandas as pd
import json
import os

path = 'data/map/user/hover/country/india/state/'
state_list = os.listdir(path)

clm = {
    'State': [], 
    'Year': [], 
    'Quarter': [],
    'District': [], 
    'RegisteredUsers': [], 
    'AppOpens': []
}

for state in os.listdir(path):
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                hover_data = data.get('data', {}).get('hoverData', {})
                for district, value in hover_data.items():
                    clm['State'].append(state.title().replace('-', ' '))
                    clm['Year'].append(int(year))
                    clm['Quarter'].append(int(file.strip('.json')))
                    clm['District'].append(district)
                    clm['RegisteredUsers'].append(value.get('registeredUsers', 0))
                    clm['AppOpens'].append(value.get('appOpens', 0))

Map_User = pd.DataFrame(clm)
print(Map_User)
Map_User.to_csv('map_user.csv', index=False)
