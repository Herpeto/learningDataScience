import pandas as pd
import requests
from sqlalchemy import create_engine

def extract(url):
    data = requests.get(url).json()
    
    return pd.DataFrame(data)

def transform(df):
    new_df = df.copy()
    new_df = new_df[["domains","name"]]
    new_df["domains"] = new_df["domains"].apply(lambda x:x[0])
    
    return new_df

def load(df,database_name,table_name):
    db_name =  'sqlite:///'+ database_name
    disk_engine = create_engine(db_name)

    df.to_sql(table_name, disk_engine, if_exists='replace', index=False)
    # df_check = pd.read_sql(table_name,disk_engine)
    # print(df_check)


def main():
    df = extract('http://universities.hipolabs.com/search?country=Indonesia')
    new_df = transform(df)
    # print(new_df)
    load(new_df, 'testing.db','test_table')

if __name__ == '__main__':
    main()

