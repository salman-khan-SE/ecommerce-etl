from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from transform import transform
from extract import extract
from load import load

def extract_task():
    raw_data = extract()
    raw_data.to_csv('temp.csv', index=False)

def transform_task():
    import pandas as pd
    raw_data = pd.read_csv('temp.csv')
    clean_data= transform(raw_data)
    clean_data.to_csv('clean_temp.csv', index= False)

def load_task():
    import pandas as pd
    clean_data = pd.read_csv('clean_temp.csv')
    load(clean_data)


dag = DAG(
    dag_id= 'ECOMMERCE_ETL',
    start_date= datetime(2025,5,25),
    schedule='@once',
    catchup=False
)

extract_step = PythonOperator(
    task_id = 'extract_task',
    python_callable=extract_task,
    dag= dag
)

transform_step = PythonOperator(
    task_id = 'transform_task',
    python_callable=transform_task,
    dag = dag
)

load_step = PythonOperator(
    task_id = 'load_task',
    python_callable=load_task,
    dag = dag
)

extract_step >> transform_step >> load_step