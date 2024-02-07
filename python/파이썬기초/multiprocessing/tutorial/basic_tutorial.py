import concurrent.futures
import time

# 작업 함수 정의
def task(name):
    print(f"Task {name} 시작")
    time.sleep(2)
    print(f"Task {name} 완료")

# ThreadPoolExecutor 생성
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 작업을 submit 메서드로 '제출'
    # 제출하면 작업이 시작된다.
    futures = [executor.submit(task, i) for i in range(6)]
    print("제출 완료") # 작업이 시작되면서 메인 프로세스는 다음 코드를 실행함

    concurrent.futures.wait(futures) # 작업이 완료될 때까지 대기
    print("모든 작업 완료")




    