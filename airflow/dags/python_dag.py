#~/airflow/dags/dummy.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'anthony',
    'depends_on_past': True,
    'retries': 3, 
    'retry_delay': timedelta(seconds=30),
}

dag = DAG(
    'python_main_pipeline',
    default_args = default_args,
    description = 'Dummy Pipeline for Airflow Testing ',
    schedule_interval='*/15 * * * *',  # Runs every 15 minutes
    start_date = datetime(2024, 1, 1),
    catchup = False,
)

import os
os.chdir('/opt/airflow/scripts')
from main import main

func_process_csv  = main(process_csv = True)
func_test_api  = main(process_csv = True)

task_process_csv = PythonOperator(
    task_id='task_process_csv',
    python_callable=func_process_csv,
    dag=dag,
)

task_test_apis = PythonOperator(
    task_id='task_test_apis',
    python_callable=func_test_api, 
    dag=dag,
)

# Define task dependencies
task_process_csv >> task_test_apis