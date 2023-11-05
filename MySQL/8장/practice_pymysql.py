import pymysql


with open('pw.txt', 'r') as f:
    pw = f.readline()

# sql 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password=pw, db='soloDB', charset='utf8')

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS userTabel")

cur.execute("CREATE TABLE  IF NOT EXISTS userTable (\
    id char(4), \
    userName char(15), \
    email char(20), \
    birthYear int)")

cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)")
cur.execute("INSERT INTO userTable VALUES('kim', '김태연', 'kim@naver.com', 2011)")
cur.execute("INSERT INTO userTable VALUES('star', '별사랑', 'star@naver.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('yang', '양지은', 'yang@naver.com', 1992)")

conn.commit()
conn.close()



