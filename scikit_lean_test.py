# 必要なライブラリーのインポート
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# データフレームの作成
movie = pd.read_csv('movie.csv')
#print(movie)

#インスタンス
linear_regression = LinearRegression()

#説明変数を縦(1)の列と指定し,削除
X = movie[["budget"]].values

#Y 目的変数
Y = movie[["revenue"]].values
print(X)
print("ashdjhgzfhdjhshtstr")
print(Y)

#学習
linear_regression.fit(X, Y)  

print('coefficient = ', linear_regression.coef_[0]) # 説明変数の係数を出力
print('intercept = ', linear_regression.intercept_) # 切片を出力

coefficient =  9.10210898118
intercept =  -34.6706207764


plt.scatter(X, Y, color = 'blue')         # 説明変数と目的変数のデータ点の散布図をプロット
plt.plot(X, linear_regression.predict(X), color = 'red') # 回帰直線をプロット

plt.title('Regression Line')               # 図のタイトル
plt.xlabel('Average number of rooms [budget]') # x軸のラベル
plt.ylabel('Prices in $1000\'s [revenue]')    # y軸のラベル
plt.grid()                                 # グリッド線を表示

plt.show()                                 # 図の表示
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