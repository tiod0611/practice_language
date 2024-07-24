import pandas as pd
import time, os, requests
import warnings
import datetime

url = "https://www.dabangapp.com/api/3/new-room/detail?api_version=3.0.1&call_type=web&room_id=6688c17aab02da65a9820495&version=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)
data = response.json()['room']

df = pd.DataFrame(
    data=data.values(),
    columns=data.keys()
)

print(df)