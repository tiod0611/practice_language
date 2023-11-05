import pymysql


class DBUpdater:
    def __init__(self, db_pw):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password=db_pw
        )

        with conn.cursor() as cursor:
            sql = "CREATE DATABASE IF NOT EXISTS attendance_db"
            cursor.execute(sql)
        
        conn.commit()

        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password=db_pw,
            db='attendance_db',
        )

        with self.conn.cursor() as cursor:
            sql = f"""
            CREATE TABLE IF NOT EXISTS Attendance_book(
            id INT NOT NULL AUTO_INCREMENT,
            user VARCHAR(255),
            day DATE,
            time TIME,
            weekday INT,
            PRIMARY KEY(id)
            );
            """
            cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def replace_into_row(self, user, now_datetime):

        with self.conn.cursor() as cursor:
            sql = f"""
            REPLACE INTO Attendance_book(user, day, time, weekday) VALUES(
            '{user}',
            '{now_datetime[0]}', 
            '{now_datetime[1]}',
            '{now_datetime[2]}'
            );"""
            cursor.execute(sql)
        self.conn.commit()