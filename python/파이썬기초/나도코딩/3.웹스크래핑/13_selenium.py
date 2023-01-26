from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.get("http://naver.com")

elem = driver.find_element(By.XPATH, '//*[@id="account"]/a')

elem.click()
driver.back()
driver.refresh()

elem = driver.find_element(By.ID, "query")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = driver.find_elements(By.TAG_NAME, "a")

# for i in elem:
#     print(i.get_attribute("href"))

driver.get("http://daum.net")
elem = driver.find_element(By.ID, "q")
elem.send_keys("나도코딩")
elem = driver.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
elem.click()

driver.quit()
