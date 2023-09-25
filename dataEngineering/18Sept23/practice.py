from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
import pandas as pd
import numpy as np

# Custom Function
def change_gender(x):
    if(x == 'Pria'):
        x = 'L'
    else:
        x = 'P'
    return x


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
df = pd.DataFrame()

# DEFINE TASKS

def print_msg():
    print('Halo selamat datang di DAG ini!')

def create_data():
    data = {
        'Name' : ['Andi','Budi','Chandrika','Danila','Eko','Fani'],
        'Age': [21,32,27,15,24,22],
        'Gender':['Pria','Pria','Wanita','Wanita','Pria','Wanita']
    }
    df = pd.DataFrame(data)
    
def trans_data():
    df['Gender'] = df['Gender'].apply(change_gender)

task_1 = PythonOperator(
    task_id = 'task1',
    python_callable = print_msg,
    dag = dag
)

task_2 = PythonOperator(
    task_id = 'task2',
    python_callable = create_data,
    dag = dag
)

task_3 = PythonOperator(
    task_id = 'task3',
    python_callable = trans_data,
    dag = dag
)

# DEFINE DEPENDENCIES
task_1 >> task_2
task_2 >> task_3