import json
import os
import pandas as pd
import pymongo

def extract(path):
    '''
    json 파일을 로드하는 함수
    '''
    with open(path) as f:
        json_ = json.load(f)

    return json_

# task 1 : 
def get_keyword(obs):
    '''
    키워드와 카테고리 정보 추출
    '''
    keyword = obs['keyword']
    category = obs['category']

    return keyword, category

def save_keyword(dataframe, keyword, category):
    '''
    키워드와 카테고리를 저장
    '''
    pass

# task 2 : 
def is_win_game(reward):
    '''
    무승부 혹은 err 가 있는지 검사
    없다면 승자가 있는 게임
    '''
    if None in reward or -1 in reward:
        return False
    else :
        return True
    

def get_matadata(sliced_dict, id):
    '''
    메타 데이터를 뽑아내는 함수
    '''

    # episode_id 
    episode_id = id # file name 자체가 episode id이므로

    # is_win 
    is_win = True if -1 not in sliced_dict['rewards'] else False

    # players
    rewards = sliced_dict['rewards']
    win_player_idx = [idx for idx, s in enumerate(rewards) if s > 0]
    win_questioner = sliced_dict['info']['TeamNames'][win_player_idx[0]]
    win_answerer = sliced_dict['info']['TeamNames'][win_player_idx[1]]

    # rewards 
    reward = rewards[win_player_idx[0]]

    # rounds 
    rounds = 22 - reward
    
    values = [episode_id, is_win, rewards, win_player_idx, win_questioner, win_answerer, reward, rounds]
    return win_player_idx, values

def save_metadata():
    '''
    메타데이터를 저장하는 함수
    '''
    pass

def get_episode_data(obs):
    '''
    우승자의 경기 대화를 추출하는 함수
    '''
    questions = obs['questions']
    answers = obs['answers']
    guesses = obs['guesses']

    return questions, answers, guesses

def save_episode_data():
    '''
    에피소드를 저장하는 함수
    '''
    pass

def main():
    path = './data/episode/JSONs/'
    file_list = os.listdir(path)

    for file in file_list:
        id = int(file.split('.')[0]) 
        json_ = extract(path+file)
        obs = json_['steps'][-1][-1]['observation']['keyword']
        
        keyword, category = get_keyword(obs)

        # 키워드 저장 