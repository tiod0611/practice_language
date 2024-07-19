from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

import sys, os
# sys.path.append(os.getcwd())

# 현재 파일의 디렉토리 경로를 얻습니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
# 상위 폴더 경로를 얻습니다.
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
# 상위 폴더 경로를 sys.path에 추가합니다.
sys.path.insert(0, parent_dir)
env_path = os.path.join(parent_dir, '.env')

from utils.slack_alert import SlackAlert
from MLproject.titanic import *
from dotenv import load_dotenv

titanic = TitanicMain()

load_dotenv(dotenv_path=env_path)
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
slack = SlackAlert("#tutorialairflow-alarm", SLACK_TOKEN)

def print_result(**kwargs):
    r = kwargs['task_instance'].xcom_pull(key='result_msg')
    print("message : ", r)

default_args = {
    'owner': 'Tiod',
    'depends_on_past': False,
    'email': ['tiod0611@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
}

dag_args = dict(
    dag_id='tutorial_with_slack-bot',
    default_args=default_args,
    description='airflow에 slack bot을 심어서 메시지를 받아보자',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2024, 1, 1),
    tags=['tutorial', 'slack'],
    on_success_callback=slack.success_msg,
    on_failure_callback=slack.fail_msg
)

with DAG( **dag_args ) as dag:
    start = BashOperator(
        task_id='start',
        bash_command='echo "start!"',
    )

    prepro_task = PythonOperator(
        task_id='preprocessing',
        python_callable=titanic.prepro_data,
        op_kwargs={'f_name': "train"}
    )
    
    modeling_task = PythonOperator(
        task_id='modeling',
        python_callable=titanic.run_modeling,
        op_kwargs={'n_estimator': 100, 'flag' : True}
    )

    msg = PythonOperator(
        task_id='msg',
        python_callable=print_result
    )

    complete = BashOperator(
        task_id='complete_bash',
        bash_command='echo "complete~!"',
    )

    start >> prepro_task >> modeling_task >> msg >> complete

