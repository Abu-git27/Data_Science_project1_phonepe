import os
import json
import pandas as pd

path = 'data/aggregated/user/country/india/state/'

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Brand': [],
    'RegisteredUsers': [],
    'AppOpens': []
}

state_list = os.listdir(path)
for state in state_list:
    state_path = os.path.join(path, state)
    if not os.path.isdir(state_path):
        continue
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        if not os.path.isdir(year_path):
            continue
        for file in os.listdir(year_path):
            if not file.endswith('.json'):
                continue
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)

                aggregated = data.get('data', {}).get('aggregated', {})
                app_opens = aggregated.get('appOpens', 0)

                users_by_device = data.get('data', {}).get('usersByDevice')
                if users_by_device:
                    for device in users_by_device:
                        clm['State'].append(state)
                        clm['Year'].append(int(year))
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['Brand'].append(device.get('brand', 'Unknown'))
                        clm['RegisteredUsers'].append(device.get('count', 0))
                        clm['AppOpens'].append(app_opens)

Device_Users = pd.DataFrame(clm)
print(Device_Users)
Device_Users.to_csv('device_user.csv', index=False)
