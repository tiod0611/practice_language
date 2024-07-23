import os

from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def upload_to_s3(filename: str, key: str, bucket_name: str) -> None:
    hook = S3Hook('aws_s3_test')
    if hook.check_for_key(key, bucket_name):
        print(f"The key {key} already exists in bucket {bucket_name}.")
    else:
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")
        hook.load_file(filename=filename, key=key, bucket_name=bucket_name, replace=False)
        print(f"Uploaded {filename} to bucket {bucket_name} with key {key}.")
    
def dowload_from_s3(local_path: str, key: str, bucket_name: str) -> None:
    hook = S3Hook('aws_s3_test')
    if os.path.isfile(local_path):
        print(f"The file {local_path} already exists.")
        return
    hook.download_file(key=key, bucket_name=bucket_name, local_path=local_path, preserve_file_name=True)

with DAG(
    'upload_to_s3',
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2024, 1, 1),
    catchup = False,
) as dag:
    upload = PythonOperator(
        task_id = 'upload',
        python_callable= upload_to_s3,
        op_kwargs={
            'filename':'/home/ubuntu/airflow/upload_test.txt',
            'key' : 'test/upload_test.txt',
            'bucket_name' : 'tiod-wabh-test',
        }
    
    )

    download = PythonOperator(
        task_id = 'downlaod',
        python_callable=dowload_from_s3,
        op_kwargs={
            'key' : 'test/upload_test.txt',
            'bucket_name' : 'tiod-wabh-test',
            'local_path' : 'data/',
        }
    )

    upload >> download 