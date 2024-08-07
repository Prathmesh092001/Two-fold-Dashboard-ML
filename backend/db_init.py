import pandas as pd
from sqlalchemy import create_engine
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Read data from Excel files
files = ['5308.xlsx', '5329.xlsx']
for file in files:
    df = pd.read_excel(f'../data/{file}', sheet_name=None)
    for sheet_name, sheet_data in df.items():
        sheet_data.to_sql(sheet_name, engine, if_exists='replace', index=False)

print("Data loaded into PostgreSQL successfully")
