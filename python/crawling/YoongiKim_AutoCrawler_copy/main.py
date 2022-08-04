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

    @staticmethod
    def get_keywords(keywords_file='keywords.txt'):
        # 파일에서 검색 키워드 읽기
        with open(keywords_file, 'r', encoding='utf-8-sig') as f:
            # utf-8-sig는 기존 utf-8에서 BOM을 출력할 때 문제가 발생하기 때문에 이를 회피하는 방법이다.
            # BOM을 제거하고 출력한다.
            text = f.read()
            lines = text.split('\n')
            lines = filter(lambda x: x !='' and x is not None, lines) # lines가 없는 경우가 아닐 때
            keywords = sorted(set(lines))

        print('{} keywords found: {}'.format(len(keywords), keywords))

        # re-save sorted keywords
        with open(keywords_file, 'w+', encoding='utf-8') as f:
            # w+ vs w : w는 쓰기 전용, w+는 읽고 쓰기
            for keyword in keywords:
                f.write('{}\n'.format(keyword)) 
        
        return keywords
    
    @staticmethod
    def save_object_to_file(object, file_path, is_base64=False):
        try:
            with open('{}'.format(file_path), 'wb') as file:
                if is_base64:
                    file.write(object)
                else:
                    shutil.copyfileobj(object.raw, file)
        
        except Exception as e:
            print('Save failed - {}'.format(e))

    @staticmethod
    def base64_to_object(src):
        header, encodered = str(src).split(',', 1)
        data = base64.decodebytes(bytes(encoded, encoding='utf-8'))
        return data

    def download_image(self, keyword, links, site_name, max_count=0):
        self.make_dir('{}/{}'.format(self.download_path, keyword.replace('"', '')))
        total = len(links)
        success_count = 0

        if max_count == 0: # 무한대로 다운 받게 설정했다면
            max_count = total
        
        for index, link in enumerate(links):
            if success_count >= max_count:
                break

            try:
                print('Downloading {} from {}: {} / {}'.format(keyword, site_name, success_count + 1, max_count))

                if str(link).startswith('data:image/jpeg;base64'): # 문자열이 다음으로 시작한다면 => Bool
                    response = self.base64_to_object(link)
                    ext = 'jpg'
                    is_base64 = True

                elif str(link).startswith('data:image/png;base64'):
                    response = self.base64_to_object(link)
                    ext = 'png'
                    is_base64 = True
                else:
                    response = requests.get(link, stream=True)
                    ext = self.get_extension_from_link(link)
                    is_base64 = False
                
                no_ext_path = '{}/{}/{}_{}'.format(self.download_path.replace('"', ''), keyword, site_name,
                                                    str(index).zfill(4))

                path = no_ext_path + '.' + ext
                self.save_object_to_file(response, path, is_base64=is_base64)

                success_count += 1
                del response

                ext2 = self.validate_image(path)
                
                if ext2 is None:
                    print('Unreadable file - {}'.format(link))
                    os.remove(path)
                    success_count -= 1
                else:
                    if ext != ext2:
                        path2 = no_ext_path + '.' + ext2
                        os.rename(path, path2)
                        print('Renamed extension {} -> {}'.format(ext, ext2))

            except Exception as e:
                print('Download failed - ', e)
                continue
    
    def download_from_site(self, keyword, site_code):
        site_name = Sites.get_text(site_code)
        add_url = Sites.get_face_url(site_code) if self.face else ""

        try:
            proxy = None
            if self.proxy_list:
                proxy = random.choice(self.proxy_list)
            
            collect = CollectLinks(no_gui=self.no_gui, proxy=proxy) # 크롬 드라이버 초기화
        except Exception as e:
            print("Error occurred while initializing chromedriver - {}".format(e))
            return
        
        try:
            print('Collecting links... {} from {}'.format(keyword, site_name))
            
            if site_code == Sites.GOOGLE:
                links = collect.google(keyword, add_url)
            elif site_code == Sites.NAVER:
                links = collect.naver(keyword, add_url)
            elif site_code == Sites.GOOGLE_FULL:
                links = collect.google_full(keyword, add_url)
            elif site_code == Sites.NAVER_FULL:
                links = collect.naver_full(keyword, add_url)
            else:
                print("Invalid site code")
                links = []
            
            print('Downloading images from collected links... {} from {}'.format(keyword, site_name))
            self.download_image(keyword, links, site_name, max_count=self.limit)
            Path('{}/{}/{}_done'.format(self.download_path, keyword.replace('"',''), site_name)).touch()

            print('Done {} : {}'.format(site_name, keyword))

        except Exception as e:
            print("Exception {}:{} - {}".format(site_name, keyword, e))

    def download(self, args):
        self.download_from_site(keyword=args[0], site_code=args[1])
    