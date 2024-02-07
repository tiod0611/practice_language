from concurrent import futures
# Reuse functions in flags.py
from flags import save_flag, get_flag, main


# 하나의 국기 이미지를 다운받는 함수. 각 worker가 이 함수를 수행함
def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f'{cc}.git')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    # context manager로서 ThreadPoolExecutor를 인스턴스화 함.
    # executor.__exit__() 메소드는 executor.shutdown(wait=True)를 호출하는데,
    # 이는 스레드가 완료될때까지 Block을 시킴
    with futures.ThreadPoolExecutor(max_workers=None) as executor:
        # map 메소드는 내장 함수 map과 유사함
        # 첫 번째 인수인 download_one 함수는 여러 스레드에서 동시에 호출됩니다.
        # map 메소드는 각 함수 호출에서 리턴되는 값들을 반복할 수 있는 제너레이터를 반환합니다.
        # 여기서는 country code를 반홤함
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))

if __name__=='__main__':
    # 이 스크립트에서 구현한 download_many 콜러블을 인수로 전달하여,
    # flags.py에서 구현한 main 함수 호출
    main(download_many)