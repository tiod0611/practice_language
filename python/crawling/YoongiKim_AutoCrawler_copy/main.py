from lib2to3.pgen2.pgen import PgenGrammar
import os
import requests
import shutil # 파일과 관련된 고수준 연산을 제공. 특히, 파일 복사와 삭제를 지원하는 함수 제공
from multiprocessing import Pool
import argparse
from collect_links import CollectLinks 
import imghdr # 이미지 유형 판단
import base64 # 이 모듈은 바이너리 데이터를 인쇄 가능한 ASCII 문자로 인코딩하고 이러한 인코딩을 다시 바이너리 데이터로 디코딩하는 함수를 제공합니다
from pathlib import Path
import random

class Sites:
    GOOGLE = 1
    NAVER = 2
    GOOGLE_FULL = 3
    NAVER_FULL = 4

    @staticmethod
    def get_text(code):
        if code == Sites.GOOGLE:
            return 'google'
        elif code == Sites.NAVER:
            return 'naver'
        elif code == Sites.GOOGLE_FULL:
            return 'google'
        elif code == Sites.NAVER_FULL:
            return 'naver'


    @staticmethod
    def get_face_url(code):
        if code == Sites.GOOGLE or Sites.GOOGLE_FULL:
            return "&tbs=itp:face" # // 이게 뭘까? url에 붙는 것 같은데
        if code == Sites.NAVER or Sites.NAVER_FULL:
            return "&face=1"             

class AutoCrawler:
    def __init__(self, skip_already_exist=True, n_threads=4, do_google=True, do_naver=True, download_path='download', full_resolution=False, face=False, no_gui=False, limit=0, proxy_list=None):
        
        """
        :param skip_already_exist: 이미 다운로드한 키워드는 스킵함. re-downloding에 필요함
        :param n_threads: 다운로드 하는 threads의 수
        :param do_google: 구글에서 다운로드(boolean)
        :param do_naver: 네이버에서 다운로드(boolean)
        :param download_path: 다운로드 되는 경로
        :param full_resolution: 이미지 섬네일 대신 원본 해상도로 다운로드함(느림)
        :param face: Face search mode
        :param no_gui: GUI 모드 사용 안함. full_resolution mode를 가속함
        :param limit: 다운로드 이미지 개수 지정 (0으로 할시 무한대로 다운함)
        :param proxy_list: 프록시 리스트. 모든 thread는 리스트에서 랜덤하게 하나를 선택함
        """

        self.skip = skip_already_exist
        self.n_threads = n_threads
        self.do_google = do_google
        self.do_naver = do_naver
        self.download_path = download_path
        self.full_resolution = full_resolution
        self.face = face
        self.no_gui = no_gui
        self.limit = limit
        self.proxy_list = proxy_list if proxy_list and len(proxy_list) > 0 else None # 한개 이상의 원소가 있는 경우에만

        os.makedirs('./{}'.format(self.download_path), exist_ok=True) # eist_ok 해당 dir이 있으면 생성 없으면 지나감
    
    @staticmethod
    def all_files(path):
        paths = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.isfile(path + '/' + file):
                    paths.append(path + '/' + file)
        
        return paths

    @staticmethod
    def get_extension_from_link(link, default='jpg'):
        splits = str(link).split('.')
        if len(splits) == 0:
            return default
        ext = splits[-1].lower()
        if ext == 'jpg' or ext == 'jpeg':
            return 'jpg'
        elif ext == 'gif':
            return 'gif'
        elif ext == 'png':
            return 'png'
        else:
            return default

    @staticmethod
    def make_dir(dirname):
        current_path = os.getcwd()
        path = os.path.join(current_path, dirname)
        if not os.path.exists(path):
            os.makedirs(path)

