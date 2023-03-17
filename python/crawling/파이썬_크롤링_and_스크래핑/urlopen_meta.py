import re
import sys
import io
from urllib.request import urlopen

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
# bytes 자료형의 응답 본문을 일단 변수에 저장함
bytes_content = f.read()

# charset은 HTML의 앞부분에 적혀 있는 경우가 많으므로
# 응답 본문의 앞부분 1024bytes를 ASCII 문자로 디코딩해 둠
# ASCII 범위 이외의 문자는 U+FFFD(REPLACEMENT CHARECTER)로 변환되어 예외가 발생하지 않음.

scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

# 디코딩한 문자열에서 정규 표현식으로 carset 값을 추출함
match = re.search(r'charset=["\']?([\w-]+)', scanned_text) 

if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'


# 추출한 인코딩을 표준 오류에 출력함
print('encoding:', encoding, file=sys.stderr)

# 추출한 인코딩으로 다시 디코딩함
text = bytes_content.decode(encoding)
print(text)