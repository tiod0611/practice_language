import sqlite3

conn = sqlite3.connect('top_cities.db')
c = conn.cursor()


# 저장한 데이터를 추출함
c.execute('SELECT * FROM cities')
# 쿼리의 결과는 fetchall() 메서드로 추출할 수 있음

for row in c.fetchall():
    # 추출한 데이터를 출력함
    print('rank: ', row[0])
    print('city: ', row[1])
    print('population: ', row[2])


# 연결 종료
conn.close()