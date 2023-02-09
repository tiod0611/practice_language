from selenium import webdriver
from selenium.webdriver import ChromeOptions
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from user_agent import generate_user_agent

# generate user_agent
userAgent = generate_user_agent(os='win', device_type="desktop")

options = ChromeOptions()
options.add_argument('--headless')
options.add_argument(f'user_agent={userAgent}')

driver_path = chromedriver_autoinstaller.install()

driver= webdriver.Chrome(driver_path, options=options)
driver.maximize_window()

driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
user_agent_value = driver.find_element(By.XPATH, '//*[@id="detected_value"]/a')

print(user_agent_value.text)