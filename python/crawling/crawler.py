import pandas as pd
import os
import re

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

def crawling(id):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=chrome_options)
    url = "https://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode={}".format(id)
    driver.get(url)

    title = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/h1/strong')
    sub_title = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/h1/span/strong')
    author = driver.find_elements(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/div[2]/span[1]')
    translater = driver.find_elements(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/div[2]/span[3]')
    publiser = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/div[2]/span[5]/a')
    date = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/div[2]/span[7]')
    mean_score = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/form/div[1]/div[3]/div/div/em')
    isbn_13 = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[5]/div/div[3]/table/tbody/tr[1]/td/span[1]')
    isbn_10 = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[5]/div/div[3]/table/tbody/tr[1]/td/span[2]')
    category_1 = driver.find_elements(by=By.XPATH, value='//*[@id="container"]/div[5]/div/div[3]/ul/li')

    print(title.text)
    print(sub_title.text)
    print([x.text for x in author])
    print([x.text for x in translater])
    print(publiser.text)
    print(date.text)
    print(mean_score.text)
    print(isbn_13.text)
    print(isbn_10.text)
    print([x.text for x in category_1][0].split(' > '))

    driver.close()

if __name__ == "__main__":
    crawling("9788960518117")