import requests
import json
import csv
import pandas as pd

#TMDB_APIから必要な情報を取得してきて、CSVファイルを作成するコード

#APIkeyを非表示にする
# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token= os.environ.get("API_KEY") # 環境変数の値をAPに代入


class TMDB:
    def __init__(self, token):
        
        self.token =token
        self.headers_ = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json;charset=utf-8'}        
        self.base_url_ = 'https://api.themoviedb.org/3/'
        self.img_base_url_ = 'https://image.tmdb.org/t/p/w500'

    def _json_by_get_request(self, url, params={}):
        #print(self.headers_)
        res = requests.get(url, headers=self.headers_, params=params)
        return json.loads(res.text)  

    def search_movies(self, query):
        params = {'query': query}
        url = f'{self.base_url_}search/movie'#f文字列でフォーマット
        return self._json_by_get_request(url, params)      

    def get_movie(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}'
        #print(url)
        return self._json_by_get_request(url)

    def get_movie_account_states(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}/account_states'
        return self._json_by_get_request(url)    

    def get_movie_alternative_titles(self, movie_id, country=None):
        url = f'{self.base_url_}movie/{movie_id}/alternative_titles'
        return self._json_by_get_request(url)    

    def get_movie_changes(self, movie_id, start_date=None, end_date=None):
        url = f'{self.base_url_}movie/{movie_id}'
        return self._json_by_get_request(url)    

    def get_movie_credits(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}/credits'
        return self._json_by_get_request(url)   

    def get_movie_external_ids(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}/external_ids'
        return self._json_by_get_request(url)

    def get_movie_images(self, movie_id, language=None):
        url = f'{self.base_url_}movie/{movie_id}/images'
        return self._json_by_get_request(url)        

    def get_movie_keywords(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}/keywords'
        return self._json_by_get_request(url)    

    def get_movie_release_dates(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}/release_dates'
        return self._json_by_get_request(url)

    def get_movie_videos(self, movie_id, language=None):
        url = f'{self.base_url_}movie/{movie_id}/videos'
        return self._json_by_get_request(url)

    def get_movie_translations(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}/translations'
        return self._json_by_get_request(url)

    def get_movie_recommendations(self, movie_id, language=None):
        url = f'{self.base_url_}movie/{movie_id}/recommendations'
        return self._json_by_get_request(url)

    def get_similar_movies(self, movie_id, language=None):
        url = f'{self.base_url_}movie/{movie_id}/similar'
        return self._json_by_get_request(url)

    def get_movie_reviews(self, movie_id, language=None):
        url = f'{self.base_url_}movie/{movie_id}/reviews'
        return self._json_by_get_request(url)

    def get_movie_lists(self, movie_id, language=None):
        url = f'{self.base_url_}movie/{movie_id}/lists'
        return self._json_by_get_request(url)

    def get_latest_movies(self, language=None):
        url = f'{self.base_url_}movie/latest'
        return self._json_by_get_request(url)

    def get_now_playing_movies(self, language=None, region=None):
        url = f'{self.base_url_}movie/now_playing'
        return self._json_by_get_request(url)

    def get_popular_movies(self, language=None, region=None):
        url = f'{self.base_url_}movie/popular'
        return self._json_by_get_request(url)

    def get_top_rated_movies(self, language=None, region=None):
        url = f'{self.base_url_}movie/top_rated'
        return self._json_by_get_request(url)

    def get_upcoming_movies(self, language=None, region=None):
        url = f'{self.base_url_}movie/upcoming'
        return self._json_by_get_request(url)


import time

# 時間計測開始
time_sta = time.time()
# 処理を書く（ここでは1秒停止する）
time.sleep(1)
# 時間計測終了


api = TMDB(token) # tokenは発行された文字列を代入

count=0
body=[]
num = 550
while count<500:
    try:
        movie = api.get_movie(num)
        if movie["budget"]!=0 and movie["revenue"]!=0:
            body.append([movie["id"],movie["budget"],movie["revenue"]])
            count+=1
        num+=1
    except:
        print(num)
        num +=1


header = ["id",'budget', 'revenue']
print("total:  "+str(count))
with open('movie.csv', 'w') as f:
 
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerows(body)

f.close()

"""#pandasでの実装
df=pd.DataFrame(body,columns=header)
df.to_csv('movie.csv')
"""
time_end = time.time()
# 経過時間（秒）
tim = time_end- time_sta

print(tim)

