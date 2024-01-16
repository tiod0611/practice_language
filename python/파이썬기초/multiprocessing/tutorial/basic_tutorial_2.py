import concurrent.futures
import time
import random

db = []

def simple_task(name):
    # sleep_time = random.randint(1, 2)
    print(f"Task {name} 시작")
    time.sleep(10)
    print(f"Task {name} 완료")

    return f"task:{name}-완료"

def save_data(data):
    time.sleep(2)
    db.append(data)
    print(f"{data} -> 저장 완료")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 작업을 submit 메서드로 제출
    i = [x for x in range(5)]
    result = executor.map(simple_task, i) 
    try:
        executor.map(save_data(result), result)
    except Exception as e:
        print(f"에러 발생{e}")

# 어떻게 동시에 여러 작업을 처리하지?