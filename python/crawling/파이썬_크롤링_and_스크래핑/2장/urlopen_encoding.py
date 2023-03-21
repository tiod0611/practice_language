# -*- coding: utf-8 -*-

import sys
from urllib.request import urlopen
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# HTTP 헤더를 기반으로 인코딩 방식을 추출함( 명시돼있지 않을 경우 utf-8을 사용)
encoding = f.info().get_content_charset(failobj='utf-8')

# 인코딩 방식을 표준 오류에 출력함.
print('encoding:', encoding, file=sys.stderr)

# 추출한 인코딩 방식으로 디코딩함
text = f.read().decode(encoding)

# 웹 페이지의 내용을 표준 출력에 출력함
print(text)