import time
from time import sleep

from bs4 import BeautifulSoup
import requests
import random

max_page = 11
base_url = 'http://books.toscrape.com/catalogue/page-'
urls = [base_url+str(page)+'.html' for page in range(1 , max_page)]

def get_book_urls(url: str):
    book_urls = []
    request = requests.get(url)
    sleep(0.2)

    parsed_html = BeautifulSoup(request.text, 'html.parser')
    li_element_tags = parsed_html.find_all("li", attrs={"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for tag in li_element_tags:
        book_urls.append(tag.find('a')['href'])

    print("Number of book: ", len(book_urls))
    return book_urls

def do_html_crawl(url: str):
    url = base_url + url
    reqeust = requests.get(url)
    sleep(0.2)
    parsed_html = BeautifulSoup(reqeust.text, 'html.parser')
    return parsed_html

if __name__ == "__main__":
    start_time = time.time()
    for url in urls:
        book_url_list = get_book_urls(url)
        for book_url in book_url_list:
            do_html_crawl(book_url)

    print("--- elapsed time %s seconds ---" %(time.time() - start_time)) 
    # 138 sec