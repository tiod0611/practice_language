import pymysql

with open('pw.txt', 'r') as f:
    pw = f.readline()

# 전역변수 선언부
conn, cur = None, None 
data1, data2, data3, data4 = '', '', '', ''
sql = ''

# sql 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password=pw, db='soloDB', charset='utf8')
cur = conn.cursor()

# 메인코드
cur.execute('SELECT * FROM userTable')

print('사용자ID  사용자 이름  이메일  출생연도')
print('=======================================')

while True:
    row = cur.fetchone()
    if row == None:
        break

    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]

    print(f'{data1}  {data2}  {data3}  {data4}')

# 디비 연결 종료
conn.close()