from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe", options=options)
# 1. 네이버 이동
driver.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = driver.find_element(By.XPATH, '//*[@id="account"]/a')
elem.click()

# driver.back()
# driver.refresh()

# elem = driver.find_element(By.ID, "query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# elem = driver.find_elements(By.TAG_NAME, "a")

# # for i in elem:
# #     print(i.get_attribute("href"))

# driver.get("http://daum.net")
# elem = driver.find_element(By.ID, "q")
# elem.send_keys("나도코딩")
# elem = driver.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
# elem.click()

# driver.quit()

# 3.로그인 위치 가져오기
login_id = driver.find_element(By.XPATH, '//*[@id="id"]')
login_pw = driver.find_element(By.XPATH, '//*[@id="pw"]')
login_bt = driver.find_element(By.CLASS_NAME, 'btn_login')

# 3-2. 로그인 정보 입력하고 클릭
login_id.send_keys("gyul611")
login_pw.send_keys("123123")

login_pw.clear()
login_pw.send_keys("1234")

login_bt.click()

print(driver.page_source) # html 정보를 출력

driver.quit()


