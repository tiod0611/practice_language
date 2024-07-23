from datatime import datatime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigget_rule import TriggerRule


import sys, os
sys.path.insert(0, os.getcwd())

from MLproject.titanic import *

titanic = TitanicMain()

def print_result(**kwargs):
    r = kwargs['task_instance'].xcom_pull(key='result_msg')
    print("message : ", r)


default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
}

dag_args = dict(
    dag_id="tutorial-ml-op",
    default_args=default_args,
    description='tutorial DAG ml',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2022, 2, 1),
    tags=['example-sj'],
)