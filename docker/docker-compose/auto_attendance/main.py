import datetime as dt
import argparse
from dotenv import load_dotenv
import os

from DBController import DBUpdater


def write_datetime():
    day = dt.datetime.today().strftime("%Y-%m-%d")
    time = dt.datetime.today().strftime("%H:%M:%S")
    weekday = dt.datetime.now().weekday()

    return [day, time, weekday]


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, help="write down the your name.")

    args = parser.parse_args()
    user = args.user

    load_dotenv()
    db_pw = os.environ['DB_PW']

    # 날자 정보 가져오기
    now_datetime = write_datetime()

    # DBUpdater 객체 생성
    dbupdater = DBUpdater(db_pw)

    # 데이터 기록
    dbupdater.replace_into_row(user, now_datetime)
    

