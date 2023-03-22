from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import _thread
import time

def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^/wiki/)((?!:).)*$'))
