import pandas as pd
from sqlalchemy import create_engine
import os

username = 'root'
password = '12345'  
host = 'localhost'
port = 3306
database = 'phonepe_data'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

csv_files = {
    'agg_insurance': 'agg_insurance.csv',
    'agg_transaction': 'agg_transaction.csv',
    'agg_user': 'agg_user.csv',
    'map_insurance': 'map_insurance.csv',
    'map_transaction': 'map_transaction.csv',
    'map_user': 'map_user.csv',
    'top_insurance': 'top_insurance.csv',
    'top_transaction': 'top_transaction.csv',
    'top_user': 'top_user.csv',
}

for table_name, filename in csv_files.items():
    csv_path = os.path.join(filename)
    if os.path.exists(csv_path):
        print(f"Loading {filename} into table `{table_name}`...")
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Successfully loaded: {table_name}")
    else:
        print(f"File not found: {filename}")
