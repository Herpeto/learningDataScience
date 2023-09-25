import pandas as pd
import numpy as np

df = pd.DataFrame()

def change_gender(x):
    if(x == 'Pria'):
        x = 'L'
    else:
        x = 'P'
    return x

# DEFINE TASKS

def print_msg():
    print('Halo selamat datang di DAG ini!')

def create_data():
    df['Name'] = ['Andi','Budi','Chandrika','Danila','Eko','Fani']
    df['Age'] = [21,32,27,15,24,22]
    df['Gender'] = ['Pria','Pria','Wanita','Wanita','Pria','Wanita']
    print(df)
    
def trans_data():
    df['Gender'] = df['Gender'].apply(change_gender)

print_msg()
create_data()
trans_data()


print(df)