from time import sleep
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import concurrent.futures
import requests
import time

max_page = 134
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

def do_thread_crawl(urls: list):
    thread_list = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            thread_list.append(executor.submit(do_html_crawl, url))
        for execution in concurrent.futures.as_completed(thread_list):
            execution.result()

def do_process_with_thread_crawl(url: str):
    
    (get_book_urls(url))

if __name__ == "__main__":
    start_time = time.time()

    with Pool(processes=10) as pool:
        pool.map(do_process_with_thread_crawl, urls)
        pool.terminate()
        pool.join()
    print("--- elapsed time %s seconds ---" %(time.time() - start_time))
    # 7 sec 