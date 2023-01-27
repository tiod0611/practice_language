from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options =webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe", options=options)

driver.maximize_window() #창 최대화

url = 'https://flight.naver.com/'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')

time.sleep(3)