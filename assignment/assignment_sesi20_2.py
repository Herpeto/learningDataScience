from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
import pandas as pd
import numpy as np
import requests
from sqlalchemy import create_engine

# DEFAULT ARGUMENTS
default_args = {
    'owner':'airflow',
    'start_date':datetime(2023,9,18),
    'end_date':datetime(2023,9,18,12),
    'retries':1,
    'retry_delay':timedelta(minutes=2)
}

# DAG INITIATION
dag = DAG(
    dag_id='practice_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5)
)

# DEFINE TASKS
def extract():
    url = 'https://raw.githubusercontent.com/ardhiraka/DEBlitz/master/day3/2.%20transform/scooter.csv'
    data = requests.get(url).json()
    
    return pd.DataFrame(data)

df = extract()

def transform0():
    # Drop region_id column
    df = df.drop('region_id',axis=1)

    # Lowercase all columns name
    df.columns= df.columns.str.lower()

    # Change format for 'started_at' to datetime
    df['started_at'] = pd.to_datetime(df['started_at'])

def loadCsv0():
    df.to_csv('data_clean.csv')

def transform1():
    new_df = df.loc[(df['started_at'] >= '2019-5-23')
                 & df['started_at'] <= '2019-6-3']
    return new_df

new_df = transform1()

def loadCsv1():
    new_df.to_csv('may23-june3.csv')

def loadSql():
    # Load after Transform Section
    database_name = 'filtered_data.db'
    table_name = 'filtered_table'
    db_name =  'sqlite:///'+ database_name

    disk_engine = create_engine(db_name)
    new_df.to_sql(table_name, disk_engine, if_exists='replace', index=False)

extract_data = PythonOperator(
    task_id = 'extract',
    python_callable = extract,
    dag = dag
)

transform_0 = PythonOperator(
    task_id = 'transform0',
    python_callable = transform0,
    dag = dag
)

load_csv_0 = PythonOperator(
    task_id = 'load_Csv0',
    python_callable = loadCsv0,
    dag = dag
)

transform_1 = PythonOperator(
    task_id = 'transform1',
    python_callable = transform1,
    dag = dag
)

load_csv_1 = PythonOperator(
    task_id = 'load_Csv1',
    python_callable = loadCsv1,
    dag = dag
)

load_sql = PythonOperator(
    task_id = 'load',
    python_callable = loadSql,
    dag = dag
)

# DEFINE DEPENDENCIES
extract_data >> transform_0 >> load_csv_0 >> transform_1 >> load_csv_1 >> load_sql