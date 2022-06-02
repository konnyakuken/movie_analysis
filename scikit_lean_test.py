# 必要なライブラリーのインポート
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

# データフレームの作成
movie = pd.read_csv('movie.csv')
#print(movie)

print(movie.iloc[:, 0:100])


#インスタンス
#linear_regression = LinearRegression()

#説明変数を縦(1)の列と指定し,削除
X = movie.drop("budget", 1)

#Yに目的変数を入れます！
Y = movie.drop("revenue", 1)
print(X)
print("ashdjhgzfhdjhshtstr")
print(Y)

#こんな書き方でも大丈夫！
#Y = boston_df["PRICE"]
"""
# ライブラリーのインポート
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 学習データと評価データを作成
x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, 0:13], df.iloc[:, 13],
                                                    test_size=0.2, random_state=1)

#データを標準化
sc = StandardScaler()
sc.fit(x_train) #学習用データで標準化
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
"""