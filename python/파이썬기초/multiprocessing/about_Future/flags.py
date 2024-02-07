# This code is sourced from here that https://junstar92.tistory.com/362#concurrent-web-downloads.

import time
from pathlib import Path
from typing import Callable #

import requests

POP20_CC = ('KR IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://fluentpython.com/data/flags'
DEST_DIR = Path('download') # The directory with the flag images # 폴더가 없으면 새로 생성함

# img 바이트를 DEST_DIR의 filename으로 저장
def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img) #  이 문법은 뭐지
    # DEST_DIR와 filename을 결합하여 새로운 경로를 생성

# 주어진 country code로 URL을 구축하고 requests를 사용해 이미지를 다운받음
# 응답은 바이너리 데이터를 반환함
def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif' .lower() # .lower() 소문자로 변환
    resp = requests.get(url)
    return resp.content

# loop를 돌며 알파벳 순으로 각 country code에 맞는 이미지를 다운받음( 핵심 함수)
def download_many(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ' , flush=True)
    return len(cc_list)

# main 함수는 다운로드를 수행하는 함수를 인수로 받아서 호출됨
# 이 함수는 다른 스크립트에서도 사용됨
def main(download: Callable[[list[str]], int]) -> None: 
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = download(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} download in {elapsed:.2f}s')

if __name__=='__main__':
    main(download_many)