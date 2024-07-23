'''
경로와 데이터 핸들링에 필요한 설정값
'''

import os
import pathlib

class PathConfig:
    def __init__(self):
        '''
        경로 초기화
        '''

        # 현재 파일이 위치한 디렉토리의 절대 경로를 가져옴.
        self.project_path = pathlib.Path(__file__).parent.resolve() 
        # 프로젝트 경로를 기반으로 titanic 데이터 디렉토리 경로를 구함.
        self.titanic_path = f"{self.project_path}/data/titanic"

class EnvConfig:
    def get_gender_mapping_code(self):
        gender_mapping_info = {
            'male' : 0,
            'female' : 1,
        }

        return gender_mapping_info
    
    def get_column_list(self):
        column_list = ['Sex', 'Age_band', 'Pclass']
        return column_list 