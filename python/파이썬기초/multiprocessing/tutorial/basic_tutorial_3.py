import concurrent.futures
import time
import random

def generate_data(name):
    print(f"Task 1 ({name}) - 데이터 생성 시작")

    time.sleep(random.randint(1, 10))
    data = f"데이터_{name}"
    print(f"Task 1 ({name}) - 데이터 생성 완료")
    # return data
    # save_to_database(data)

def save_to_database(data):
    print(f"    >> Task 2 - 데이터 저장 시작: {data}")
    time.sleep(1)
    print(f"    >> Task 2 - 데이터 저장 완료")

data_name = ["A", "B", "C", "D"]
if __name__=="__main__":
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # map 메서드를 사용하여 두 가지 다른 task 함수 처리
        # result_task1 = executor.map(generate_data, data_name)
        # result_task2 = executor.map(save_to_database, result_task1)
        futures_task1 = [executor.submit(generate_data, name) for name in data_name]

        #Task 2를 병렬로 실행하면서 Task 1이 완료될 때까지 대기
        for future_task1 in concurrent.futures.as_completed(futures_task1):
            data_task1 = future_task1.result()
            executor.submit(save_to_database, data_task1)