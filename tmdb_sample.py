import tmdbsimple as tmdb
import csv

#APIkeyを非表示にする
# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token= os.environ.get("API_v3_auth") # 環境変数の値をAPに代入

"""
def movie_info_collecti():
	tmdb.API_KEY = token
	num = 2
	while num < 580:
        try:
            movie = tmdb.Movies(num)
            response = movie.info()
            if movie.budget!=0 and movie.revenue!=0:
                print("('" + movie.title + "', '" + str(movie.id) + "', '" + str(movie.budget) + "', '"+str(movie.revenue)+","+str(movie.genres)+"," + movie.release_date + "', '" + str(movie.runtime) + "', '" + "https://image.tmdb.org/t/p/w500{}".format(movie.poster_path) + "'),")
                num = num + 1
        except:
            print(num)
            num = num + 1
            pass
"""
body=[]
import time

# 時間計測開始
time_sta = time.time()
# 処理を書く（ここでは1秒停止する）
time.sleep(1)
# 時間計測終了


tmdb.API_KEY = token
num = 550
while num < 580:
    try:
        movie = tmdb.Movies(num)
        response = movie.info()
        if movie.budget!=0 and movie.revenue!=0:
            body.append([movie.id,movie.budget,movie.revenue])
            #print("('" + movie.title + "', '" + str(movie.id) + "', '" + str(movie.budget) + "', '"+str(movie.revenue)+","+str(movie.genres)+"," + movie.release_date + "', '" + str(movie.runtime) + "', '" + "https://image.tmdb.org/t/p/w500{}".format(movie.poster_path) + "'),")
        num+=1
    except:
        print(num)
        num +=1
        pass


header = ["id",'budget', 'revenue']
print(body)

time_end = time.time()
# 経過時間（秒）
tim = time_end- time_sta

print(tim)