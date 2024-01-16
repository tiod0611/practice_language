import threading
import queue
import time
import random

# Task 1: 데이터 생성
def generate_data(name):
    print(f"Task 1 ({name}) - 데이터 생성 시작")
    time.sleep(random.uniform(1, 3))
    data = f"데이터_{name}"
    print(f"Task 1 ({name}) - 데이터 생성 완료")
    return data

# Task 2: 데이터 저장
def save_to_database(data):
    print(f"Task 2 - 데이터 저장 시작: {data}")
    time.sleep(random.uniform(2, 4))
    print(f"Task 2 - 데이터 저장 완료")

# 작업을 스케줄링하는 함수
def task_scheduler(worker_queue):
    while True:
        task, args = worker_queue.get()
        if task is None:
            break
        task(*args)

# 데이터 생성에 사용할 인자들
data_names = ['A', 'B', 'C', 'D']

# 스레드 풀 생성 (2개의 worker를 생성)
worker_queue = queue.Queue()
worker_threads = []

for _ in range(2):
    thread = threading.Thread(target=task_scheduler, args=(worker_queue,))
    worker_threads.append(thread)
    thread.start()

# Task 1을 worker 1에게, Task 2를 worker 2에게 할당
for name in data_names:
    worker_queue.put((generate_data, (name,)))
    worker_queue.put((save_to_database, (name,)))

# 모든 작업이 완료될 때까지 대기
worker_queue.join()

# 모든 worker에게 종료 명령 전달
for _ in range(2):
    worker_queue.put((None, None))

# 모든 worker 스레드가 종료될 때까지 대기
for thread in worker_threads:
    thread.join()