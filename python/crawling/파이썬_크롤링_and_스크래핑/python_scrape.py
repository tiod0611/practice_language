import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def fetch(url):
    """
    매개변수로 전달받을 url을 기반으로 웹 페이지를 추출함
    웹 페이지의 인코딩 형식은 Content-Type 헤더를 기반으로 알아냄
    반환값: str 자료형의 HTML
    """
    
    f = urlopen(url)
    # HTTP 헤더를 기반으로 인코딩 형식을 추출
    encoding = f.info().get_content_charset(failobj='utf-8')
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩
    html = f.read().decode(encoding)
    return html

def scrape(html):
    """
    매개변수 html로 받은 HTML을 기반으로 정규 표현식을 사용해 도서 정보를 추출함
    """
    books = []
    # re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출
    # re.DOTALL은 정규식에서 .이 \n도 매치되도록 해준다.
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        # 도서의 url을 추출함
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr'+url

        # 태그를 제거해서 도서의 제목을 추출함
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)

        books.append({'url': url, 'title': title})
    return books

def save(db_path, books):
    """
    매개변수 books로 전달된 도서 목록을 SQLite3로 저장함
    데이터베이서의 경로는 매개변수 db_path로 지정함
    반환값: None(없음)
    """

    # db 연결

    conn = sqlite3.connect(db_path)

    # cursor 추출
    c = conn.cursor()
    # execute() 메서드로 SQL 실행
    # 스크립트를 여러 번 실행할 수 있으므로 기존의 books 테이블을 제거함
    c.execute('DROP TABLE IF EXISTS books')
    # books 테이블을 생성함
    c.execute('''
        CREATE TABLE books(
            title text,
            url text
        )
    ''')

    # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있음
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    # commit
    conn.commit()

    conn.close()

def main():
    """
    메인 처리
    fetch(), scrape(), save() 함수를 호출함.
    """

    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save('books.db', books)


if __name__=='__main__':
    main()