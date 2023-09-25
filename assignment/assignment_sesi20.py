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
    url = 'http://universities.hipolabs.com/search?country=Indonesia'
    data = requests.get(url).json()
    
    return pd.DataFrame(data)

df = extract()

def transform():
    # Transform Section
    new_df = df.copy()
    new_df = new_df[["domains","name"]]
    new_df["domains"] = new_df["domains"].apply(lambda x:x[0])
    return new_df
    
new_df = transform()

def load():
    # Load after Transform Section
    database_name = 'filtered_data.db'
    table_name = 'filtered_table'
    db_name =  'sqlite:///'+ database_name

    disk_engine = create_engine(db_name)
    new_df.to_sql(table_name, disk_engine, if_exists='replace', index=False)

extract = PythonOperator(
    task_id = 'extract',
    python_callable = extract,
    dag = dag
)

transform = PythonOperator(
    task_id = 'transform',
    python_callable = transform,
    dag = dag
)

load = PythonOperator(
    task_id = 'load',
    python_callable = load,
    dag = dag
)

# DEFINE DEPENDENCIES
extract >> transform >> load