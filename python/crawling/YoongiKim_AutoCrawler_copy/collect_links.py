from telnetlib import EC
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException
import platform
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions ad EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os.path as osp

class CollectLinks:
    def __init__(self, no_gui=False, proxy=None):
        executable = ''

        if platform.system() == 'Windows':
            print('Detected OS : Windows')
            executable = './chromedriver/chromedriver_win.exe'
        elif platform.system() == 'Linux':
            print('Detected OS: Linux')
            executable = './chromedriver/chromedriver_linux'
        elif platform.system() == 'Darwin':
            print('Detected OS: Mac')
            executable = './chromedriver/chromedriver_mac'
        else:
            raise OSError('Unknown OS Type')
        
        if not osp.exists(executable):
            raise FileNotFoundError('Chromedriver file should be placed at {}'.format(executable))
        
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        if no_gui:
            chrome_options.add_argument('--headless')
        if proxy:
            chrome_options.add_argument('--proxy-server={}'.format(proxy))
        
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        browser_version = 'Failed to detect version'
        chromedriver_version = 'Failed to detect version'
        major_version_different = False

        if 'browserVersion' in self.browser.capabilities:
            browser_version = str(self.browser.capabilities['browserVersion'])

        if 'chrome' in self.browser.capabilities:
            if 'chromedriverVersion' in self.browser.capabilities['chrome']:
                chromedriver_version = str(self.browser.capabilities['chrome']['chromedriverVersion']).split(' ')[0]
        
        if browser_version.split('.')[0] != chromedriver_version.split('.')[0]:
            major_version_different = True
        
        print('_________________________')
        print('Current web-browser version:\t{}'.format(browser_version))
        print('Current chrome-driver version:\t{}'.format(chromedriver_version))
        if major_version_different:
            print('warning: Version different')
            print('Download correct version at "http://chromedriver.chromium.org/downloads" and place in "./chromedriver"')
            print('_________________________')

    
    def get_scroll(self):
        pos = self.browser.execute_script("return window.pageYOffset;")
        return pos
    
    def wait_and_click(self, xpath):
        # 가끔 이유 없이 클릭이 실패할 때, 어떻게든 클릭을 시도함
        try:
            w = WebDriverWait(self.browser, 15)
            elem = w.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elem.click()
            self.highlight(elem)
        except Exception as e:
            print('Click time out - {}'.format(xpath))
            print('Refreshing browser...')
            self.browser.refresh()
            time.sleep(2)
            return self.wait_and_click(xpath)
        
        return elem
    
    def highlight(self, element):
        self.browser.execute_script("arguments[0].setAttributie('style', arguments[1];", element, 
                                    "backgroud: yellow; border: 2px solid red;")
    
    @staticmethod
    def remove_duplicates(_list):
        return list(dict.fromkeys(_list))

    def google(self, keyword, add_url=""):
        self.browser.get("https://www.google.com/search?q={}&source=lnms&tbm=isch{}".format(keyword, add_url))

        time.sleep(1)

        print('Scrolling down')

        elem = self.browser.find_element(By.TAG_NAME, 'body')

        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

        try:
            self.wait_and_click('//input[@type="button"]')

            for i in range(60):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.2)

        except ElementNotVisibleException:
            pass

        photo_grid_boxes = self.browser.find_elements(By.XPATH, '//div[@class="bRMDJf islir"]')

        print('Scriping links')

        links = []

        for box in photo_grid_boxes:
            try:
                imgs = box.find_elements(By.TAG_NAME, 'img')

                for img in imgs:
                    src = img.get_attribute('src')

                    if str(src).startswith('data'):
                        src = img.get_attribute("data-iurl")
                    links.append(src)

            except Exception as e:
                print('[Exception occurred while collecting links from google {}'.format(e))

        links = self.remove_duplicates(links)
        print('Collect links done. Site: {}, Keyword: {}, Total: {}'.format('google', keyword, len(links)))
        self.browser.close()

        return links

    def naver(self, keyword, add_url=""):
        self.browser.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}{}".format(keyword,add_url))
    
        time.sleep(1)

        print('Scrolling down')

        elem = self.browser.find_element(By.TAG_NAME, "body")

        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

        imgs = self.browser.find_elements(By.XPATH, '//div[@class="photo_bx api_ani_send _photoBox"]//img[@class="_image _listImage"]')
        print('Scrolling links')

        links = []

        for img in imgs:
            try:
                src = img.get_attribute("src")
                if src[0] != 'd':
                    links.append(src)
                
            except Exception as e:
                print('[Exception occured while collecting links from naver] {}'.format(e))

        
        links = self.remove_duplicates(links)

        print('Collect links done. Site: {}, Keyword: {}, Total: {}'.format('naver', keyword, len(links)))
        self.browser.close()

        return links

        