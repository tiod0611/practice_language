from concurrent import futures
from flags import save_flag, get_flag, main

def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    cc_list = cc_list[:5] # 5개의 나라만 사용
    # 대기 중인 Future를 살펴보기 위해 max_workers를 3으로 설정
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            # submit은 콜러블이 실행되도록 스케쥴링하고 이 작업을 나타내는 Future를 반환함
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')
        
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f'{future} result: {res!r}')
    
    return count

if __name__ == "__main__":
    main(download_many)