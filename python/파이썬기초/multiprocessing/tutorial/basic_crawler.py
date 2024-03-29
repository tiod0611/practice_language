from fake_useragent import UserAgent

import time
from time import sleep

from multiprocessing import Pool
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from selenium import webdriver

import urllib.request
import requests


urls = ["https://namu.wiki/w/%EB%B6%84%EB%A5%98:%EC%A0%95%EC%88%98", 
        'https://namu.wiki/w/%EB%B6%84%EB%A5%98:%EC%88%98', 
        'https://namu.wiki/w/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%20%EC%95%84%EC%9D%B4%EB%8F%8C', 
        'https://namu.wiki/w/%EB%B6%84%EB%A5%98:%EA%B1%B8%EA%B7%B8%EB%A3%B9']


def get_sublist_href(url: str):
    namu_link = []
    request = requests.get(url) 
    sleep(1)

    parsed_html = BeautifulSoup(request.text, 'html.parser')
    a_element_tags = parsed_html.find_all('div', attrs={'class':'_5pchnzVo'})

    for tag in a_element_tags:
        for link in tag.find_all('a'):
            if 'href' in link.attrs:
                namu_link.append(url+str(link['href']))

    print("Number of site: ", len(namu_link))
    return namu_link

def do_html_crawl(url: str):
    request = requests.get(url)
    sleep(1)
    parsed_html = BeautifulSoup(request.text, 'html.parser')
    return parsed_html

if __name__ == "__main__":
    start_time = time.time()
    for url in urls:
        sub_url_list = get_sublist_href(url)
        for sub_url in sub_url_list:
            do_html_crawl(sub_url)
    
    print("--- elapsed time %s seconds ---" %(time.time() - start_time)) 
    # 93 seconds
    # 259