import pandas as pd
import requests
from sqlalchemy import create_engine

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    return float(x)    

def extract(file_name):
    # Baca File dari File CSV
    df = pd.read_csv(file_name)
    
    return df

def transform(df):
    # Buat Data Copyan
    new_df = df.copy()

    # Cek apakah ada missing values
    # Apabila rata-rata missing values berada diatas 80% per kolomnya, maka akan di drop kolom tersebut
    null_above_8 = (new_df.isnull().mean() > 0.8)
    new_df = new_df.drop((null_above_8[null_above_8] == True).index, axis=1)

    # Ubah format harga menjadi angka
    # Ambil Currency dan buat jadi satu kolom baru
    new_df["Currency"] = new_df["Wage"].str[0]

    # Delete Currency dari Kolom yang ada
    new_df["Value"] = new_df["Value"].str.replace("€","")
    new_df["Wage"] = new_df["Wage"].str.replace("€","")
    new_df["Release Clause"] = new_df["Release Clause"].str.replace("€","")

    # Ubah dari K dan M menjadi 1000 dan 1000000
    new_df["Value"] = new_df["Value"].apply(value_to_float)
    new_df["Wage"] = new_df["Wage"].apply(value_to_float)
    new_df["Release Clause"] = new_df["Release Clause"].apply(value_to_float)

    # Hapus Enter yang ada pada Nama Tim
    new_df["Club"] = new_df["Club"].str.replace('\n\n\n\n', '')

    # Pisahkan Kolom Contract
    new_df[['Contract_Start', 'Contract_End']] = new_df['Contract'].str.split(' ~ ', expand=True)

    # Hapus Kolom Contract
    new_df = new_df.drop("Contract", axis=1)
    
    return new_df

def load(df,database_name,table_name):
    db_name =  'sqlite:///'+ database_name
    disk_engine = create_engine(db_name)

    df.to_sql(table_name, disk_engine, if_exists='replace', index=False)
    # df_check = pd.read_sql(table_name,disk_engine)
    # print(df_check)


def main():
    df = extract('fifa21 raw data v2.csv')
    new_df = transform(df)
    load(new_df, 'testing.db','test_table')

if __name__ == '__main__':
    main()