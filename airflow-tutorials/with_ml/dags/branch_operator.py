from datetime import datetime, timedelta  # timedelta는 뭐임?
from textwrap import dedent  # textwrap? 문자열을 감싸는 기능일 것 같다.
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator # type: ignore 
# dummy 오퍼레이터는 말 그대로 더미임. 사전에 주로 구조를 짤 때 많이 쓰인다고 함.
from airflow.operators.python import BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule


# 파이썬 함수를 호출하는 예시임.
# def random_branch_path():
#     # 필요 라이브러리는 각 함수 아래에 위치시키라고 하네.
#     from random import randint

#     return "path_1" if randint(1, 2) == 1 else "path_2"

def random_branch_path():
    import random
    branches = ['path_1', 'print_hello_in_english']
    chosen_branch = random.choice(branches)
    print(f"Choosing branch: {chosen_branch}")
    return chosen_branch


# 기본 arg 설정
default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,  # 실패시 재시도 횟수
    'retry_delay': timedelta(minutes=15),  # 재시도 간격
}

# DAG에 대한 설정
dag_args = dict(
    dag_id='branch_operator-tutorial',
    default_args=default_args,
    description='operator 분기에 대한 튜토리얼 입니다.',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2024, 1, 1),
    tags=['branch', 'tutorials']  # dag의 태그구나

)


# with 구문으로 DAG 정의
with DAG(**dag_args) as dag:

    # t1, t2 그리고 t3를 instantiating operators로 Tasks를 생성하는 예제임
    t1 = BashOperator(
        task_id='print_date',
        bash_command='echo "오늘은 ${date}입니다."',
    )

    # 여기서 나오는 결과에 따라 다음 task_id로 이동함.
    t2 = BranchPythonOperator(
        task_id='choice_branch',
        # 파이썬 함수가 들어감. 그런데 인자를 받으려면 어떻게 하지?? 다른 예제에서 나오겠지.
        python_callable=random_branch_path,
    )

    t3 = BashOperator(
        task_id='print_hello_in_korean',
        depends_on_past=False,  # 이게 무슨 의미지?
        bash_command='echo "안녕하세요."'
    )

    t4 = BashOperator(
        task_id='print_hello_in_english',
        depends_on_past=False,  # 이전 operator의 성공 여부와 관계없이 실행됨.
        bash_command='echo "Hi."',
    )

    complete = BashOperator(
        task_id='complete',
        depends_on_past=False,
        bash_command='echo "complete~!"',
        trigger_rule=TriggerRule.NONE_FAILED
    )

    dummy_1 = DummyOperator(task_id='path_1')

    t1 >> t2 >> dummy_1 >> t3 >> complete
    t1 >> t2 >> t4 >> complete
