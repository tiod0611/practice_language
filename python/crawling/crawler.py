import pandas as pd
import os
import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def crawling(id):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=chrome_options)
    url = "https://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode={}".format(id)
    driver.get(url)

    title = driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[1]/h1/strong')
    sub_title = driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[1]/h1/span/strong')
    author = driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[1]/div[3]/span[1]')
    translater = driver.find_element('//*[@id="container"]/div[2]/form/div[1]/div[3]/span[3]/a')
    publiser = driver.find_element('//*[@id="container"]/div[2]/form/div[1]/div[3]/span[5]/a')
    date = driver.find_element('//*[@id="container"]/div[2]/form/div[1]/div[3]/span[7]')
    mean_score = driver.find_element('//*[@id="container"]/div[2]/form/div[1]/div[4]/div/div/em')
    isbn = driver.find_element('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr[1]/td/span[1]')
    category_1 = driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/ul')

    print(title.text)
    print(sub_title.text)
    print(author.text)
    print(translater.text)
    print(publiser.text)
    print(date.text)
    print(mean_score.text)
    print(isbn.text)
    print(category_1.text)

    driver.close()

if __name__ == "__main__":
    crawling("9788960518117")