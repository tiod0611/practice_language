from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

dag_args = dict(
    dag_id="python-op-tutorials_with-xcom",
    default_args=default_args,
    description='xcom과 함께 branch 튜토리얼',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2022, 2, 1),
    tags=['example-sj'],
)

# python 함수 정의
def random_branch_path():
    from random import randint

    return "cal_a_id" if randint(1, 2) == 1 else "cal_m_id"

def cal_add(x, y, **kwargs):
    result = x + y
    print("x + y : ", result)
    kwargs['task_instance'].xcom_push(key='calc_result', value=result) # xcom 이 결과는 다른 task인 print_result에서 실행될 것임.
    return "calc add"

def cal_mul(x, y, **kwargs):
    result = x * y
    print("x * y: ", result)
    kwargs['task_instance'].xcom_push(key='calc_result', value=result) # xcom
    return "calc mul"

def print_result(**kwargs):
    r = kwargs['task_instance'].xcom_pull(key='calc_result') # 여기서 push된 값을 pull 함. 이때 key값으로 가져옴.
    print("message : ", r)
    print("*"*100)
    print(kwargs)

def end_seq():
    print("========== end ==========")



with DAG(**dag_args)as dag:
    start = BashOperator(
        task_id = 'start',
        bash_command='echo "Start!"',
    )

    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=random_branch_path,
    )

    calc_add = PythonOperator(
        task_id = 'cal_a_id',
        python_callable=cal_add,
        op_kwargs={'x': 10, 'y': 4},
    )

    calc_mul = PythonOperator(
        task_id='cal_m_id',
        python_callable=cal_mul,
        op_kwargs={'x': 10, 'y': 4}
    )

    msg = PythonOperator(
        task_id='msg',
        python_callable=print_result,
        trigger_rule=TriggerRule.NONE_FAILED,
    )

    complete_py = PythonOperator(
        task_id='complete_py',
        python_callable=end_seq,
        trigger_rule=TriggerRule.NONE_FAILED,
    )

    complete = BashOperator(
        task_id='complete_bash',
        depends_on_past=False,
        bash_command='echo "complete~!"',
        trigger_rule=TriggerRule.NONE_FAILED,

    )

    start >> branch >> calc_add >> msg >> complete_py >> complete
    start >> branch >> calc_mul >> msg >> complete