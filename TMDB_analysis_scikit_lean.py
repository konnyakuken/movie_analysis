#線形回帰分析

import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# データフレームの作成
movie = pd.read_csv('movie.csv')

#インスタンス
linear_regression = LinearRegression()

#説明変数
X = movie[["budget"]].values

#Y 目的変数
Y = movie[["revenue"]].values
#print(X)
#print(Y)


# ライブラリーのインポート
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# 学習データと評価データを作成
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=1)

#データを標準化
sc = StandardScaler()
sc.fit(x_train) #学習用データで標準化
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

sc.fit(y_train) #学習用データで標準化
y_train_std = sc.transform(y_train)
y_test_std = sc.transform(y_test)
"""
from sklearn import preprocessing
#データを標準化
sscaler = preprocessing.StandardScaler()
sscaler.fit(X)
xss_sk = sscaler.transform(X) 
sscaler.fit(Y)
yss_sk = sscaler.transform(Y)
"""

#学習
linear_regression.fit(x_train_std, y_train_std)  
#linear_regression.fit(X, Y)  

# スコア計算のためのライブラリ
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

# 回帰　
pred_lr = linear_regression.predict(x_test_std)
#pred_lr = linear_regression.predict(X)

# 評価
# 決定係数(R2)
r2_lr = r2_score(y_test_std, pred_lr)
#r2_lr = r2_score(Y, pred_lr)

# 平均二乗誤差(MSE)(小さいほどモデルの誤差が少ない)
mse_lr = mean_absolute_error(y_test_std, pred_lr)
#mse_lr = mean_absolute_error(Y, pred_lr)

print("R2 : %.3f" % r2_lr)
print("MSE : %.3f" % mse_lr)


 # 説明変数の係数を出力(傾き)
print('coefficient = ', linear_regression.coef_[0])
# 切片を出力
print('intercept = ', linear_regression.intercept_) 

plt.scatter(x_test_std, y_test_std, color = 'blue')         # 説明変数と目的変数のデータ点の散布図をプロット
plt.plot(x_test_std, linear_regression.predict(x_test_std), color = 'red') # 回帰直線をプロット

plt.title('movie_analysis')               # 図のタイトル
plt.xlabel('budget') # x軸のラベル
plt.ylabel('revenue')    # y軸のラベル
plt.grid()                                 # グリッド線を表示

plt.show()

#推論 (inference) 
x_check=x_test[:3]
print(linear_regression.predict(x_check))
print("y_test=",y_test[:3])
print("x_test=",x_test[:3])

